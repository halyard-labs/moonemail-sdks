# Security

Report vulnerabilities privately to support@moonemail.co. Do not post credentials,
message contents, recipient addresses or private attachment URLs in public issues.

Use the SDKs on a server with a scoped Moonemail API key. Never embed keys in a
browser, mobile application, repository or public example. Keep TLS verification
on. A custom base URL receives the API key, so only configure trusted endpoints.

Clients do not automatically retry sends. Retry a transient error only with the
same payload and idempotency key. Respect HTTP 429 and Retry-After. API scopes,
account limits and approval requirements are enforced by Moonemail, not bypassed
by these SDKs. Download URLs and inbound message contents are untrusted input.
