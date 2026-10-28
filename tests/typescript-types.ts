import { Moonemail, type SendEmailRequestTo } from '../typescript/dist';
const scalar: SendEmailRequestTo = 'one@example.com';
const multiple: SendEmailRequestTo = ['one@example.com'];
// @ts-expect-error Recipients must not silently degrade to an empty object type.
const invalid: SendEmailRequestTo = { address: 'one@example.com' };
const client = new Moonemail('test-key');
client.emails.send({ from: 'sender@example.com', to: multiple, subject: 's', text: 't' });
client.domains.getDomainHealth({ id: 'domain-id' });
client.webhooks.listWebhookDeliveries({ id: 'webhook-id' });
void scalar; void invalid;
