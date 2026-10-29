# Moonemail JavaScript / TypeScript

Install from [npm](https://www.npmjs.com/package/moonemail): `npm install moonemail`.
Node.js 22+; use only on your server when supplying an API key.

```ts
import { Moonemail, ResponseError } from 'moonemail';

const email = new Moonemail(process.env.MOONEMAIL_API_KEY!);
const sent = await email.emails.send({
  from: 'Acme <hello@your-verified-domain.com>',
  to: ['recipient@example.com'],
  subject: 'Your receipt',
  text: 'Thanks for your order.',
}, { idempotencyKey: 'order-123-receipt' });
console.log(sent.id);

const page = await email.emails.listEmails({ limit: 20 });
const health = await email.domains.getDomainHealth({ id: 'domain-id' });
```

Generated fields use camelCase (`replyTo`, `scheduledAt`) and are serialized to
the API's snake_case fields. All generated API classes and models are also
exported. Resource properties: `emails`, `receiving`, `inboxes`, `domains`,
`apiKeys`, `webhooks`, `suppressions`, `permissions`.

```ts
try {
  await email.permissions.getPermissions();
} catch (error) {
  if (error instanceof ResponseError) {
    const status = error.response.status;
    const retryAfter = error.response.headers.get('retry-after');
    // Inspect the structured error using await error.response.json().
  }
  throw error;
}
```

For tests or custom servers, pass `{ basePath, fetchApi }` as the second
constructor argument. Each generated call also accepts a RequestInit override
(e.g. `{ signal: AbortSignal.timeout(30_000) }`). The `emails.send` convenience
accepts `signal` alongside `idempotencyKey`. No automatic send retries or hidden
pagination. Never ship the key in a browser bundle.
