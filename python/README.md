# Moonemail Python

Install the wheel linked in the [release](https://github.com/halyard-labs/moonemail-sdks/releases/tag/v0.1.0).
Python 3.10+; synchronous urllib3 transport and typed Pydantic models.

```python
import os
from moonemail import Moonemail

with Moonemail(os.environ['MOONEMAIL_API_KEY']) as email:
    sent = email.emails.send({
        'from': 'Acme <hello@your-verified-domain.com>',
        'to': ['recipient@example.com'],
        'subject': 'Your receipt',
        'text': 'Thanks for your order.',
    }, idempotency_key='order-123-receipt')
    print(sent.id)
    page = email.emails.list_emails(limit=20, _request_timeout=30)
    health = email.domains.get_domain_health('domain-id', _request_timeout=30)
```

`emails.send` accepts a wire-format dictionary or a generated `SendEmailRequest`.
The generated methods use typed models; see `docs/` for their signatures.
Resources: `emails`, `receiving`, `inboxes`, `domains`, `api_keys`, `webhooks`,
`suppressions`, `permissions`. `ApiException` exposes `status`, `headers`, and
`body`; inspect them before retrying. Reuse the idempotency key and payload.

Send convenience calls default to a 30-second timeout. Pass `_request_timeout`
to other generated methods. Constructor `base_url` is configurable for tests;
only point it at trusted servers, because it receives your key. Use the context
manager to release connections. No automatic retries or background pagination.
