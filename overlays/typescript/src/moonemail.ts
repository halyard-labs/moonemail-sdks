import { Configuration, type ConfigurationParameters } from './runtime';
import { EmailsApi, DomainsApi, InboxesApi, ReceivingApi, APIKeysApi, WebhooksApi, SuppressionsApi, PermissionsApi } from './apis';
import type { SendEmailRequest } from './models';

export type MoonemailOptions = Omit<ConfigurationParameters, 'accessToken'>;
export type SendOptions = { idempotencyKey?: string; signal?: AbortSignal };

/** Server-side client. Keep API keys out of browser bundles. No automatic send retries. */
export class Moonemail {
  readonly emails;
  readonly domains: DomainsApi;
  readonly inboxes: InboxesApi;
  readonly receiving: ReceivingApi;
  readonly apiKeys: APIKeysApi;
  readonly webhooks: WebhooksApi;
  readonly suppressions: SuppressionsApi;
  readonly permissions: PermissionsApi;

  constructor(apiKey: string, options: MoonemailOptions = {}) {
    if (!apiKey?.trim()) throw new Error('A Moonemail API key is required.');
    const config = new Configuration({ ...options, accessToken: apiKey });
    const emails = new EmailsApi(config);
    this.emails = Object.assign(emails, {
      send: (body: SendEmailRequest, options: SendOptions = {}) => emails.sendEmail(
        { sendEmailRequest: body, idempotencyKey: options.idempotencyKey },
        { signal: options.signal },
      ),
    });
    this.domains = new DomainsApi(config);
    this.inboxes = new InboxesApi(config);
    this.receiving = new ReceivingApi(config);
    this.apiKeys = new APIKeysApi(config);
    this.webhooks = new WebhooksApi(config);
    this.suppressions = new SuppressionsApi(config);
    this.permissions = new PermissionsApi(config);
  }
}
