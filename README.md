# Meta
The why, what, and how of MeltanoLabs

We want [MeltanoLabs](https://meltano.com/blog/launching-meltanolabs-your-home-for-singer-connectors-dbt-packages-and-all-meltano-plugins/) to be a resource for the Singer Community where the expectations of taps and targets are well defined and maintained for the long term.
The Singer community has a vast library of connectors but the quality, feature completeness, and maintenance vary.
MeltanoLabs is a place where new connectors, primarily built using the Meltano SDK, can be incubated and existing unmaintained connectors in the ecosystem can be migrated and upgraded to the standard that the MeltanoLabs community expects.
As part of the acceptance process for MeltanoLabs we will be requiring a level of commitment by the contributors and a minimum level of quality.
Based on the [Maintenance Statuses](#Maintenance-Statuses) we expect that most of the connectors in MeltanoLabs are in the Active (Stable) category and there's a smaller subset of connectors in the Development or Prerelease status because they were either just created or recently migrated.

## Community Roles and Responsibilities

With MeltanoLabs we hope to foster a community of contributors who are well versed in Singer and the Meltano SDK.
The three roles that exist in MeltanoLabs are maintainers, contributors, and community members.
Each one has different expectations and level of access to the repositories within MeltanoLabs.

### Community Members

Everyone who uses or contributes to connectors within MeltanoLabs are considered community members.
Community members are encouraged to use the connectors available in MeltanoLabs and to submit feedback or raise bugs as issues in the repositories.
The more community members we have that are using these connectors the faster we can spot and address bugs while also adding features that are most useful, ultimately making the connectors the best they can be.

### Contributors

MeltanoLabs contributors are community members who volunteer to actively make contributions and review pull requests/issues within MeltanoLabs repositories but don't have an explicit maintainer status on any one repository.
This group of community members will be part of the `labs` slack channel and will be the first to hear about repositories that need new maintainer volunteers and general maintenance requests.

### Maintainers

Connector maintainers are community members who have stepped up to take temporary ownership of a repository's maintenance.
Community members can volunteer to be owners of a connector for a specific duration of time.
This is much more light weight and very different from asking for full-time permanent fork owners.
The developer can support for the project scope or time duration that makes sense.
We would likely ask for a 3 months minimum commitment, and/or a commitment to meet a specific core set of functionality - such as reaching 'v1' if the connector is brand new.
The expectation is that while a maintainer has long term ownership of a repository they will promptly review issues and pull requests.
When the maintainer reaches a point where they no longer have the capacity or desire to be the maintainer anymore they can pass ownership off to another community member volunteer.


## Contributing a Connector to MeltanoLabs

MeltanoLabs is introducing the "Community-Managed Fork with Community Maintainers" [ownership model](https://gitlab.com/meltano/meta/-/issues/73) by allowing community members to share ownership of connector repositories.
The two main ways that connectors are added to MeltanoLabs right now are either by starting fresh and adding a new connector from scratch or by migrating an existing connector from a personal namespace into the shared MeltanoLabs namespace.

### Adding A New Connector

MeltanoLabs is a great place for community members to incubate connectors for new sources or destinations in a shared space to make it easier for the community to contribute and maintain it into the future after it leaves the development phase.
We also encourage community members to use this as a place where existing connectors can be rebuilt or ported over to the Meltano SDK.

See the [Connector Development Standards](connector-dev.md) guide for best practices and conventions.

If you'd like to create a new connector in MeltanoLabs, create an issue labeled "Add New Connector - [your connector name]" in the [Meta repo](https://github.com/MeltanoLabs/Meta) and assign it to @tayloramurphy and @pnadolny13 when you're code is ready to be pushed up to GitHub and they will create you a repository and give you access.
Alternatively you could build it in your own namespace and later migrate it once its ready.

### Migrating An Existing Connector

Its understandable that sometimes community members build new connector or create a fork and add features in their own namespace which then becomes the primary variant used by the community, but they no longer have the capacity or desire to maintain it.
In this case the primary maintainer has the option to migrate their connector to MeltanoLabs where it can live and be maintained into the future.

Connectors in MeltanoLabs have quality expectations. If the connector does not meet the standard then we will label it with the appropriate maintenance status in its current state and request community contributions to get it up to the Active (Stable) status we expect.

If you'd like to migrate an existing connector to MeltanoLabs create an issue labeled "Migrate Existing Connector - [your connector name]" in the [Meta repo](https://github.com/MeltanoLabs/Meta) and assign it to @tayloramurphy and @pnadolny13 with a link to the source repository you would like to migrate.
The Admins will review your repository and will give instructions on how to migrate along with necessary permissions once its been approved.
Alternatively you could build it in your own namespace and later migrate it once its ready.

### Permissions and Teams

Each repository has a GitHub team with the same name e.g. tap-x where community members can be added.
The GitHub team is a child of the generic Singer Taps/Targets team.
The team is then assigned to the repository with "maintain" permissions.
If a maintainer chooses to pass their maintenance responsibilities to another person, they are simply removed from the GitHub team to revoke privileges.

### Finding Maintainers

The initial approach will be to ask for volunteers within the MeltanoLabs community to take ownership of a repository as maintainer but we know that for some less frequently used connectors there might not be enough volunteers.

In this case we will do the following:
1. Whenever we receive a PR or Issue for a connector that has no maintainers, we announce this to the contributor.
1. We will post the PR or Issue to the MeltanoLabs contributors via the `labs` Slack channel to request community reviews. Known past contributors and maintainers will get mentioned.
1. If no one from the community responds in a timely manner, we can offer the PR author to become a contributor if they have a history of contributing to Meltano and/or other open source projects. (We can use their GitHub history to help in this evaluation process.)
1. Any successfully-merged PR automatically promotes that person to "contributor" and optionally to maintainer if they've consented in step 3 and no other maintainers exist.

### Relinquish Maintainership

One of the main reasons for the MeltanoLabs ownership model is to allow connector maintainers to come and go.
If you're a maintainer and no longer have the capacity or desire to be the maintainer anymore you can pass ownership off to another community member volunteer.

- Open an issue in this repository "Relinquish Maintainership - tap-x" and assign it to @tayloramurphy, @pnadolny13, and @afolson.
- Tag anyone who you suggest to be the next maintainer to get confirmation. It's fine if you don't have someone in mind, we will help find someone from the community.
- Create a PR to edit the [connector owner table](https://github.com/MeltanoLabs/Meta#connector-owners) in this README to remove your name and optionally add the new maintainer if one exists.
- A member of the Meltano team will remove you from the connector's GitHub team and add the new maintainer.

### Publishing to PyPI

You can request that your package be published to PyPI by opening an issue in this repository "Publish to PyPI - tap-x" and cc'ing @MeltanoLabs/meltanolabs-admin with the following information:

* Repository name, e.g. `MeltanoLabs/tap-messagebird`
* Desired package name in PyPI
* Release GitHub workflow name, e.g. `release.yml` if the workflow is in `.github/workflows/release.yml`

After a short review, the team will enable the PyPI publishing workflow for your repository and you'll be able to publish releases to PyPI by triggering the release workflow.

## Maintenance Statuses

Active (Stable): The connector repository is well maintained and recommended for use in production environments.
The repository has all of the following attributes; all known issues and bugs are addressed promptly, changes are expected to go through pull request reviews, releases to main are created on the appropriate cadence, security patches are addressed promptly, a CI pipeline that runs automated testing is present, community contributed pull requests are reviewed in a timely manner, README is complete with examples and detail, etc.

Prerelease (Beta): The repository was recently created and initial development is complete but hasn't been hardened enough for production environments yet.
We encourage the community to start testing out the connector and submit issues or merge requests to help get it to the Active (Stable) status.
The repository has some or all of the following attributes; most of the features are functioning but edge cases and bugs are still being addressed, changes are expected to go through pull requests and issues, some automated tests but code coverage could be low, optional CI, the README is clear and minimally complete but might be lacking in extensive detail or examples, etc.

Development (Under Construction): The repository is undergoing initial development and is not ready to be used yet.
Not recommended for use outside of development environments.
The repository has some or all of the following attributes; the developer might be regularly committing directly to the main branch, pull requests reviews are optional, no CI/CD, tests might not be passing, README might be sparse, etc.

Inactive or Stale: The repository has some or all of the following attributes; unresponsive maintainers, many unaddressed issues or pull requests, security patches are not kept up to date, unresolved failing CI pipelines, etc.

Unknown: The status of the connector is currently undefined.
We encourage community members to submit merge requests to update incorrect statuses.

See the [Connector Development Standards](connector-dev.md) guide for best practices and conventions.

## Connector Owners

Check out all the [published connectors](https://hub.meltano.com/singer/maintainers/meltanolabs) on MeltanoHub!

# Taps
|                              Connector Name                               |     Status      |                    Member/Organization Name                    |                                 MeltanoHub                                 |
|---------------------------------------------------------------------------|-----------------|----------------------------------------------------------------|----------------------------------------------------------------------------|
|[tap-linkedin-ads](https://github.com/MeltanoLabs/tap-linkedin-ads)        |Active (Stable)  |[Meltano](https://github.com/meltano) - Maintainer              |[Link](https://hub.meltano.com/extractors/tap-linkedin-ads--meltanolabs/)   |
|[tap-facebook](https://github.com/MeltanoLabs/tap-facebook)                |Active (Stable)  |[Meltano](https://github.com/meltano) - Maintainer              |[Link](https://hub.meltano.com/extractors/tap-facebook--meltanolabs/)       |
|[tap-klaviyo](https://github.com/MeltanoLabs/tap-klaviyo)                  |Active (Stable)  |[Meltano](https://github.com/meltano) - Maintainer              |[Link](https://hub.meltano.com/extractors/tap-klaviyo--meltanolabs/)        |
|[tap-kustomer](https://github.com/MeltanoLabs/tap-kustomer)                |Active (Stable)  |[Meltano](https://github.com/meltano) - Maintainer              |[Link](https://hub.meltano.com/extractors/tap-kustomer--meltanolabs/)       |
|[tap-pulumi-cloud](https://github.com/MeltanoLabs/tap-pulumi-cloud)        |Active (Stable)  |[Meltano](https://github.com/meltano) - Maintainer              |[Link](https://hub.meltano.com/extractors/tap-pulumi-cloud--meltanolabs/)   |
|[tap-athena](https://github.com/MeltanoLabs/tap-athena)                    |Active (Stable)  |[Pat Nadolny](https://github.com/pnadolny13) - Maintainer       |[Link](https://hub.meltano.com/extractors/tap-athena--meltanolabs/)         |
|[tap-circle-ci](https://github.com/MeltanoLabs/tap-circle-ci)              |Active (Stable)  |[Fran Lozano](https://github.com/franloza) - Maintainer         |[Link](https://hub.meltano.com/extractors/tap-circle-ci--meltanolabs/)      |
|[tap-csv](https://github.com/MeltanoLabs/tap-csv)                          |Active (Stable)  |[Pat Nadolny](https://github.com/pnadolny13) - Maintainer       |[Link](https://hub.meltano.com/extractors/tap-csv--meltanolabs/)            |
|[tap-dbt](https://github.com/MeltanoLabs/tap-dbt)                          |Active (Stable)  |[Edgar Ramírez](https://github.com/edgarrmondragon) - Maintainer|[Link](https://hub.meltano.com/extractors/tap-dbt--meltanolabs)             |
|[tap-github](https://github.com/MeltanoLabs/tap-github)                    |Active (Stable)  |[Eric Boucher](https://github.com/ericboucher) - Maintainer     |[Link](https://hub.meltano.com/extractors/tap-github-search--meltanolabs)   |
|                                                                           |                 |[Laurent Savaete](https://github.com/laurentS) - Maintainer     |                                                                            |
|[tap-gitlab](https://github.com/MeltanoLabs/tap-gitlab)                    |Active (Stable)  |[Meltano](https://github.com/meltano) - Maintainer              |[Link](https://hub.meltano.com/extractors/tap-gitlab--meltanolabs/)         |
|[tap-google-analytics](https://github.com/MeltanoLabs/tap-google-analytics)|Active (Stable)  |[Pat Nadolny](https://github.com/pnadolny13) - Maintainer       |[Link](https://hub.meltano.com/extractors/tap-google-analytics--meltanolabs)|
|[tap-peloton](https://github.com/MeltanoLabs/tap-peloton)                  |Active (Stable)  |[Taylor Murphy](https://github.com/tayloramurphy) - Maintainer  |[Link](https://hub.meltano.com/extractors/tap-peloton--meltanolabs/)        |
|[tap-salesforce](https://github.com/MeltanoLabs/tap-salesforce)            |Active (Stable)  |[Dan Ladd](https://github.com/dan-ladd) - Maintainer            |[Link](https://hub.meltano.com/extractors/tap-salesforce--meltanolabs/)     |
|[tap-slack](https://github.com/MeltanoLabs/tap-slack)                      |Active (Stable)  |[Stephen Bailey](https://github.com/stkbailey) - Maintainer     |[Link](https://hub.meltano.com/extractors/tap-slack--meltanolabs/)          |
|[tap-stackexchange](https://github.com/MeltanoLabs/tap-stackexchange)      |Active (Stable)  |[Edgar Ramírez](https://github.com/edgarrmondragon) - Maintainer|[Link](https://hub.meltano.com/extractors/tap-stackexchange--meltanolabs/)  |
|[tap-sqlalchemy](https://github.com/MeltanoLabs/tap-sqlalchemy)            |Prerelease (Beta)|[AJ Steers](https://github.com/aaronsteers) - Maintainer        |                                                                            |
|[tap-sftp](https://github.com/MeltanoLabs/tap-sftp)                        |Active (Stable)  |[Henning](https://github.com/radbrt) - Maintainer               |[Link](https://hub.meltano.com/extractors/tap-sftp--meltanolabs/)           |
|[tap-cloudwatch](https://github.com/MeltanoLabs/tap-cloudwatch)            |Active (Stable)  |[Pat Nadolny](https://github.com/pnadolny13) - Maintainer       |[Link](https://hub.meltano.com/extractors/tap-cloudwatch--meltanolabs/)     |
|[tap-snowflake](https://github.com/MeltanoLabs/tap-snowflake)              |Active (Stable)  |[Meltano](https://github.com/meltano) - Maintainer              |[Link](https://hub.meltano.com/extractors/tap-snowflake--meltanolabs/)      |
|[tap-postgres](https://github.com/MeltanoLabs/tap-postgres)                |Active (Stable)  |[Meltano](https://github.com/meltano) - Maintainer              |[Link](https://hub.meltano.com/extractors/tap-postgres--meltanolabs/)       |
|[tap-airbyte-wrapper](https://github.com/MeltanoLabs/tap-airbyte-wrapper)  |Active (Stable)  |[Alex Butler](https://github.com/z3z1ma) - Maintainer           |[Link](https://hub.meltano.com/extractors/tap-airbyte-wrapper--meltanolabs/)|
|[tap-messagebird](https://github.com/MeltanoLabs/tap-messagebird)          |Active (Stable)  |[Meltano](https://github.com/meltano) - Maintainer              |[Link](https://hub.meltano.com/extractors/tap-messagebird--meltanolabs/)    |
|[tap-duckdb](https://github.com/MeltanoLabs/tap-duckdb)                    |Active (Stable)  |[Meltano](https://github.com/meltano) - Maintainer              |[Link](https://hub.meltano.com/extractors/tap-duckdb--meltanolabs/)         |


# Targets
|                           Connector Name                            |     Status      |                    Member/Organization Name                    |                              MeltanoHub                              |
|---------------------------------------------------------------------|-----------------|----------------------------------------------------------------|----------------------------------------------------------------------|
|[target-snowflake](https://github.com/MeltanoLabs/target-snowflake)  |Active (Stable)  |[Meltano](https://github.com/meltano) - Maintainer              |[Link](https://hub.meltano.com/loaders/target-snowflake--meltanolabs/)|
|[target-athena](https://github.com/MeltanoLabs/target-athena)        |Active (Stable)  |[Andrew Stewart](https://github.com/andrewcstewart) - Maintainer|[Link](https://hub.meltano.com/loaders/target-athena--meltanolabs/)   |
|                                                                     |                 |[AJ Steers](https://github.com/aaronsteers) - Maintainer        |                                                                      |
|[target-csv](https://github.com/MeltanoLabs/target-csv)              |Active (Stable)  |[AJ Steers](https://github.com/aaronsteers) - Maintainer        |[Link](https://hub.meltano.com/loaders/target-csv--meltanolabs/)      |
|[target-sqlite](https://github.com/MeltanoLabs/target-sqlite)        |Active (Stable)  |[Meltano](https://github.com/meltano) - Maintainer              |[Link](https://hub.meltano.com/loaders/target-sqlite--meltanolabs/)   |
|[target-postgres](https://github.com/MeltanoLabs/target-postgres)    |Active (Stable)  |[Meltano](https://github.com/meltano) - Maintainer              |[Link](https://hub.meltano.com/loaders/target-postgres--meltanolabs/) |
|[target-yaml](https://github.com/MeltanoLabs/target-yaml)            |Active (Stable)  |[Meltano](https://github.com/meltano) - Maintainer              |[Link](https://hub.meltano.com/loaders/target-yaml--meltanolabs/)     |
|[target-jsonl-blob](https://github.com/MeltanoLabs/target-jsonl-blob)|Prerelease (Beta)|[Edgar Ramírez](https://github.com/edgarrmondragon) - Maintainer|                                                                      |
|[target-chromadb](https://github.com/MeltanoLabs/target-chromadb)    |Prerelease (Beta)|[Meltano](https://github.com/meltano) - Maintainer              |[Link](https://hub.meltano.com/loaders/target-chromadb--meltanolabs/) |
|[target-duckdb](https://github.com/MeltanoLabs/target-duckdb)        |Prerelease (Beta)|[Meltano](https://github.com/meltano) - Maintainer              |                                                                      |
