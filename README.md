# Moonemail SDKs

Official, MIT-licensed clients for Moonemail's transactional email API:

- **JavaScript / TypeScript** — Node.js 22+, browser-compatible types; use API keys only on your server.
- **Python** — Python 3.10+, synchronous client with Pydantic models.
- **Go** — Go 1.23+, context cancellation and typed request/response models.

All 36 public API operations are generated from the same contract used by
Moonemail's API reference: sending, receiving, inboxes, domains and domain health,
webhooks and delivery logs, suppressions, API keys and permissions. Dashboard
sessions, billing and OAuth consent are intentionally excluded.

## Install v0.1.1

JavaScript/TypeScript is published on [npm](https://www.npmjs.com/package/moonemail).
Python is published on [PyPI](https://pypi.org/project/moonemail/). Go uses the
module tag. Pin versions for production integrations.

```sh
npm install moonemail@0.1.1
pip install moonemail==0.1.1
go get github.com/halyard-labs/moonemail-sdks/go@v0.1.1
```

See [TypeScript](typescript/README.md), [Python](python/README.md), and
[Go](go/README.md) for usage. These SDKs are not drop-in Resend SDK replacements;
they expose Moonemail's implemented API and do not add campaigns or SMTP.

## Source of truth and regeneration

`spec/openapi.json` is a checked-in, public-only snapshot. The service's public
contract is available at https://api.moonemail.co/openapi.json; it also contains
session-only endpoints that the importer deliberately excludes. Never copy the
private application repository into this distribution.

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-codegen.txt build
python scripts/sync-spec.py                       # fetch deployed contract
# Or: python scripts/sync-spec.py --source /path/to/public/openapi.json
python scripts/generate.py
npm ci --ignore-scripts --prefix typescript
npm run build --prefix typescript
node --test tests/typescript.test.cjs
pip install ./python
python -m unittest discover -s tests -v
(cd go && go test ./... && go vet ./...)
```

The **Release new API version** workflow checks the deployed API hourly and can
be dispatched manually. A newer stable API version regenerates and tests all three
clients, commits the public snapshot, tags the release and dispatches publishing.
A changed contract without a version bump fails; an unchanged contract is a no-op.
The older manual import workflow remains available for reviewing contract changes.
See [RELEASING.md](RELEASING.md) for activation, permissions and retries.

OpenAPI Generator is pinned to 7.26.0. Generated files are never hand-edited;
small ergonomic wrappers live in `overlays/`. CI regenerates and fails on drift,
then builds, tests and packages all three SDKs. Request/response schemas are shared;
method naming follows each language (camelCase in TypeScript, snake_case in Python).

Two generator compatibility fixes are tested: disjoint string/array `anyOf`
becomes equivalent `oneOf` for recipient typing, and Python boolean enum validators
compare booleans instead of strings. The canonical contract is left unchanged.

## Behavior

- `new Moonemail(key)` / `Moonemail(key)` / `moonemail.New(key)` use `https://api.moonemail.co`.
- Pass the same idempotency key when retrying a send. Clients do **not** retry sends automatically.
- Use `after` / `before` cursors explicitly; pagination does not fetch the entire account in the background.
- TypeScript throws `ResponseError` with the HTTP response; Python raises `ApiException`; Go returns an error and HTTP response. Inspect status and `Retry-After` before retrying.
- Received content and attachments are untrusted. The SDK retrieves private download URLs but does not automatically fetch attachments or execute anything in a message.
- SDKs are pre-1.0. Pin versions and test upgrades. Python clients validate known enums; new server enum values may require an SDK update.

## Release

See [RELEASING.md](RELEASING.md). Registry publishing uses scoped OIDC trusted
publishers. No registry tokens are stored here.

Support: support@moonemail.co. See [SECURITY.md](SECURITY.md) for security reports.
