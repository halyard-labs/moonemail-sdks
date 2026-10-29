# Releasing

## Version source and automated releases

The application owns the version in `packages/contract/package.json`. Its generator
copies that version into OpenAPI. Review the contract and bump that version for
public API changes before deploying. All three SDKs share one distribution version. A new API version uses that version
or the next SDK patch, whichever is greater, so SDK-only fixes never cause reuse. Never repoint a released tag.

Once `RELEASE_AUTOMATION_ENABLED=true` is set in this repository, **Release new API
version** (`api-release.yml`) checks the deployed `/openapi.json` hourly (minute 17).
GitHub can delay scheduled runs. Use workflow dispatch for an immediate check.
It imports only API-key operations; no private service code is copied.

- Same version and identical public contract: no generation or release.
- Same version with a changed contract, or a version rollback: fail for review.
- New stable version: regenerate all clients with the pinned generator, test them,
  commit the snapshot and create `vX.Y.Z` and `go/vX.Y.Z` in one atomic push.
- Explicitly dispatch `release.yml`: GitHub-token tag pushes don't trigger workflows.

`release.yml` only builds tagged commits on main's history, verifies matching Go
and package versions, checks generation, runs transport/type tests, and installs
the exact npm tarball and Python wheel for another transport test. It saves those
artifacts plus SHA256SUMS in a GitHub Release before publishing. Retries reuse the
immutable assets and check existing registry files against their checksums.

## SDK-only fixes

For a wrapper, packaging or documentation fix, bump all `config/*.json` client
versions, regenerate, refresh the npm lockfile and run CI in a pull request. After
merging, tag the reviewed commit `vX.Y.Z` and `go/vX.Y.Z` and push both tags atomically.
The tag triggers publishing. Leave `spec/openapi.json` unchanged: it records the
API version behind that SDK, which may differ from the SDK distribution version.
The API monitor compares API versions to the previous imported contract, not to
the SDK version; an unchanged API remains a no-op after an SDK-only release.

## Registry setup

Both trusted publishers are configured. `RELEASE_AUTOMATION_ENABLED=true` and
`PYPI_PUBLISHING_ENABLED=true` enable API monitoring and both registry releases.
The setup below documents how to recreate these connections.

Create GitHub environments `npm` and `pypi`, permitting the main branch and stable
`v*` tags (the workflow validates the exact version). Configure trusted publishers:

| Registry | Project | Owner / repository | Workflow | Environment |
| --- | --- | --- | --- | --- |
| npm | moonemail | halyard-labs / moonemail-sdks | release.yml | npm |
| PyPI | moonemail | halyard-labs / moonemail-sdks | release.yml | pypi |

npm must permit direct `npm publish` for this workflow. Only the publishing jobs
receive `id-token: write`; no long-lived registry credentials are used. PyPI can
use a pending publisher before its first upload. Set `PYPI_PUBLISHING_ENABLED=true`
only after its publisher is configured. Until then Python remains installable from
the GitHub Release wheel and the PyPI job is skipped explicitly.

Enable `RELEASE_AUTOMATION_ENABLED=true` after npm's trusted publisher is configured.
A missing enabled registry version is retried on the next scheduled check. An
existing version is never overwritten. To retry explicitly:

```sh
gh workflow run release.yml --ref main -f version=0.1.1
```

Watch the workflow result and verify fresh installs from each enabled registry.
The manual **Import deployed API contract** workflow can still open a review PR;
it does not publish. Don't merge a new snapshot without its version bump.

## Distribution boundary

Only the public OpenAPI snapshot, generator/config, SDK sources, tests and docs
belong here. No service source, Terraform, deployment state, credentials or private
Git history. Mintlify hosting and SDK registry publication are separate operations.

- [npm trusted publishers](https://docs.npmjs.com/trusted-publishers/)
- [PyPI pending publishers](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/)
- [OpenAPI Generator](https://openapi-generator.tech/docs/installation/)
