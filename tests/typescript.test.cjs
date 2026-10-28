const { test } = require('node:test');
const assert = require('node:assert/strict');
const { Moonemail, ResponseError } = require(process.env.SDK_PACKAGE || '../typescript/dist');

function client(status = 200, body = { id: 'email-1' }) {
  const calls = [];
  const api = new Moonemail('test_key', { fetchApi: async (url, init) => {
    calls.push({ url, ...init });
    return new Response(JSON.stringify(body), { status, headers: { 'content-type': 'application/json', 'retry-after': '5' } });
  } });
  return { api, calls };
}

test('real transport serializes scalar and array recipients, auth, aliases and idempotency', async () => {
  const { api, calls } = client();
  for (const to of ['user@example.com', ['user@example.com']]) {
    assert.equal((await api.emails.send({ from: 'sender@example.com', to, subject: 'Hello', text: 'Body', replyTo: 'reply@example.com' }, { idempotencyKey: 'stable-key' })).id, 'email-1');
    const req = calls.at(-1);
    assert.equal(req.url, 'https://api.moonemail.co/emails');
    assert.equal(req.headers.Authorization, 'Bearer test_key');
    assert.equal(req.headers['Idempotency-Key'], 'stable-key');
    assert.deepEqual(JSON.parse(req.body), { from: 'sender@example.com', to, subject: 'Hello', text: 'Body', reply_to: 'reply@example.com' });
  }
});
test('pagination and path parameters are encoded', async () => {
  const { api, calls } = client(200, { object: 'list', data: [], has_more: false });
  await api.emails.listEmails({ limit: 2, after: 'cursor/+' });
  assert.equal(new URL(calls[0].url).searchParams.get('after'), 'cursor/+');
  await api.suppressions.removeSuppression({ email: 'a+b@example.com' });
  assert.ok(calls[1].url.endsWith('/suppressions/a%2Bb%40example.com'));
});
test('nullable permissions and future fields survive deserialization', async () => {
  const { api } = client(200, { permission: 'full_access', scopes: ['emails:send'], domain_id: null, expires_at: null, can_manage_api_keys: true, billing_requires_owner: true, future_field: 1 });
  const value = await api.permissions.getPermissions();
  assert.equal(value.domainId, null);
  assert.equal(value.expiresAt, null);
  assert.equal(value.future_field, 1);
});
test('HTTP errors expose status, response and retry-after without automatic send retry', async () => {
  const { api, calls } = client(429, { statusCode: 429, name: 'rate_limit_exceeded', message: 'Slow down' });
  await assert.rejects(api.emails.send({ from: 'a@example.com', to: 'b@example.com', subject: 's', text: 't' }), asyncError => {
    assert.ok(asyncError instanceof ResponseError);
    assert.equal(asyncError.response.status, 429);
    assert.equal(asyncError.response.headers.get('retry-after'), '5');
    return true;
  });
  assert.equal(calls.length, 1);
});
test('all public operations are represented and no dashboard API is exposed', () => {
  const fs = require('node:fs');
  const spec = require('../spec/openapi.json');
  const source = fs.readdirSync('typescript/src/apis').map(f => fs.readFileSync('typescript/src/apis/' + f, 'utf8')).join('\n');
  const operations = Object.values(spec.paths).flatMap(p => Object.values(p));
  for (const op of operations) {
    const method = op.operationId.replace(/_([a-z])/g, (_, c) => c.toUpperCase());
    assert.ok(source.includes(`async ${method}(`), method);
  }
  assert.ok(operations.length > 0);
  assert.equal(source.includes('/dashboard/'), false);
});
