# Connector Development Standards

MeltanoLabs is primarily a place for well written SDK based connectors.
As part of that there's an expected level of quality that each connector should strive to meet.
Many times the connectors in MeltanoLabs are built from scratch as a brand new connector or rebuilt to replace a legacy one.
With that in mind this is a compiled list of the development best practices and standards for adding a connector to MeltanoLabs.
This can also act as a guide for others outside the MeltanoLabs organization to understand the best approach to building a high quality connector.

## Tips For Building From Scratch

### Start With the cookiecutter Templates

When building from scratch always use the cookiecutter to make sure the newest features and recommended scaffold is present.
This is compared to starting with a clone of an existing SDK repo and modifying it for the new source, which could miss out on some improvements.

### Use the Latest SDK Version

Similarly you should always start development of a new connector using the latest SDK version.
The SDK has had major improvements over time so making sure you're taking advantage of the latest features and not accidentally reinventing the wheel is important.

### Naming Convention

Generally when deciding the name for a connector we use the `tap-<source>` naming convention.
- Start with `tap-` or `target-`
- Use dashes over underscores
- Avoid extras like `tap-<source>-sdk`, `meltano-tap-<source>`, `tap-<source>-new`, `target-<destination>-loader`, etc.
- If rebuilding an existing connector it's usually best to keep the same naming convention as existing legacy connectors for clarity within the community.
For example, prefer `tap-facebook` to `tap-meta` (Facebook's new name) because there's a long history of taps named `tap-facebook` and will be more clear.
With that consideration in mind, use your best judgement.

## Coding Standards

### Implement Integration Tests
The cookiecutter comes with default tests and the SDK has a [testing framework](https://sdk.meltano.com/en/latest/testing.html).
You should implement at least the minimum tests.

### Catalog Support

If your tap uses dynamic schema generation then you should ensure that catalog selection is supported properly.
Meltano relies on the tap to use the input catalog properly in order to support selection criteria, metadata overrides, etc.
Ensure that catalog stream, property, and metadata is respected by the tap.

### Dependency Management

- Verify that there are no extra unused dependencies in the pyproject.toml
- Dependencies for testing should go in the `dev` poetry group
- pyproject.toml package version and github/pypi release version should match
- Check for unused imports

### Other Development Tips
- General coding practices: https://handbook.meltano.com/engineering/dev-standards/
- All the TODOs from the cookiecutter should be completed and removed in initial development

## Repository Standards

- Tag git releases so users can more easily pin to a specific version.
- Enable branch protection on the default `main` branch that require PRs and code reviews in order to merge changes.
- GitHub actions CI workflow for linting and running integration pytests
- The repo has a license. Generally permissive licenses like MIT and Apache 2.0 are recommended. 
- Make sure the issues tab is enabled on repo so community members can report errors or request features

## Documentation

- `tap.py` settings are accurate and well documented. tap.py settings should reflect what should be shown on the hub. All content including: required flag, default flag, description, secret flag, etc. should be accurate in the tap.
- Auto populate the README using the `--about --format=markdown` output whenever `tap.py` settings change
- Logging, comments, doc strings, function/class/variable naming, etc. should be reviewed for clarity and accuracy
- Clearly document in the README the feature support comparison of the new tap vs the default variant on the hub and any nuances to be aware of.
- All known issues and planned improvements should be documented as issues in the repository
- Add the connector to Meta `src/connector_owners.py` and refresh the README tables
- Add to MeltanoHub
