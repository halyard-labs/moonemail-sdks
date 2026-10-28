# Releasing

1. Import the service contract with `python scripts/sync-spec.py` (or `--source`
   for a reviewed local contract), regenerate, inspect the spec/client diff, and
   open a pull request. Never edit generated types by hand.
2. Bump versions in all `config/*.json` files, regenerate, update examples and
   release links. Run the CI checks. Breaking changes require an appropriate
   version bump even when generated.
3. Build `npm pack ./typescript --pack-destination artifacts` and
   `python -m build python --outdir artifacts`. Install these exact artifacts
   in clean environments and run the transport tests before release.
4. Tag the reviewed commit `vX.Y.Z` for the distribution and `go/vX.Y.Z` for the
   Go submodule. Create a GitHub Release with the npm tarball, wheel, source
   distribution and SHA256SUMS. Release notes must identify API changes.
5. Once npm/PyPI ownership and trusted publishers are configured, publish the
   same reviewed packages there. Do not add long-lived registry tokens to this
   repository. Until then, the GitHub Release artifacts are the install source.

The public repository is a distribution boundary: only its public OpenAPI
snapshot, generator/config, SDK sources, tests and documentation belong here.
No service source, Terraform, deployment state, credentials or private Git
history. Mintlify hosting and SDK registry publication are separate operations.

Generator references (checked 28 October 2026):
- https://openapi-generator.tech/docs/installation/
- https://openapi-generator.tech/docs/generators/typescript-fetch/
- https://openapi-generator.tech/docs/generators/python/
- https://openapi-generator.tech/docs/generators/go/
