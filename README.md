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
Each one has different expectations and level of access to the respositories within MeltanoLabs.

### Community Members

Everyone who uses or contributes to connectors within MeltanoLabs are considered community members.
Community members are encouraged to use the connectors available in MeltanoLabs and to submit feedback or raise bugs as issues in the repositories.
The more community members we have that are using these connectors the faster we can spot and address bugs while also adding features that are most useful, ultimately making the connectors the best they can be.

### Contributors

MeltanoLabs contributors are community members who volunteer to actively make contributions and review pull requests/issues within MeltanoLabs repositories but dont have an explicit maintainer status on any one repository.
This group of community members will be part of the `labs` slack channel and will be the first to hear about repositories that need new maintainer volunteers and general maintenance requests.

### Maintainers

Connector maintainers are community members who have stepped up to take temporary ownership of a repository's maintainenance.
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

If you'd like to create a new connector in MeltanoLabs create an issue labeled "Add New Connector - [your connector name]" in the [Meta repo](https://github.com/MeltanoLabs/Meta) and assign it to @tayloramurphy and @pnadolny13 when youre code is ready to be pushed up to GitHub and they will create you a repository and give you access.
Alternatively you could build it in your own namespace and later migrate it once its ready.

### Migrating An Existing Connector

Its understandable that sometimes community members build new connector or create a fork and add features in their own namespace which then becomes the primary variant used by the community, but they no longer have the capacity or desire to maintain it.
In this case the primary maintainer has the option to migrate their connector to MeltanoLabs where it can live and be maintained into the future.

Connectors in MeltanoLabs have quality expectations. If the connector does not meet the standard then we will label it with the appropriate maintenance status in its current state and request community contributions to get it up to the Active (Stable) status we expect.

If you'd like to migrate an existing connector to MeltanoLabs create an issue labeled "Migrate Existing Connector - [your connector name]" in the [Meta repo](https://github.com/MeltanoLabs/Meta) and assign it to @tayloramurphy and @pnadolny13 with a link to the source repository you would like to migrate.
The Admins will review your repository and will give instructions on how to migrate along with necessary permissions once its been approved.
Alternatively you could build it in your own namespace and later migrate it once its ready.

### Permissions and Teams

TODO: define permissions using GitHub teams based on roles

### Finding Maintainers

The initial approach will be to ask for volunteers within the MeltanoLabs community to take ownership of a respository as maintainer but we know that for some less frequently used connectors there might not be enough volunteers.

In this case we will do the following:
1. Whenever we receive a PR or Issue for a connector that has no maintainers, we announce this to the contributor.
1. We will post the PR or Issue to the MeltanoLabs contributors via the `labs` Slack channel to request community reviews. Known past contributors and maintainers will get mentioned.
1. If no one from the community responds in a timely manner, we can offer the PR author to become a contributor if they have a history of contributing to Meltano and/or other open source projects. (We can use their GitHub history to help in this evaluation process.)
1. Any successfully-merged PR automatically promotes that person to "contributor" and optionally to maintainer if they've consented in step 3 and no other maintainers exist.


## Maintenance Statuses

Active (Stable): The connector repository is well maintained and recommended for use in production environments.
The repository has all of the following attributes; all known issues and bugs are addressed promptly, changes are expected to go through pull request reviews, releases to main are created on the appropriate cadence, security patches are addressed promptly, a CI pipeline that runs automated testing is present, community contributed pull requests are reviewed in a timely manner, README is complete with examples and detail, etc.

Prerelease (Beta): The repository was recently created and initial development is complete but hasnt been hardened enough for production environments yet.
We encourage the community to start testing out the connector and submit issues or merge requests to help get it to the Active (Stable) status.
The repository has some or all of the following attributes; most of the features are functioning but edge cases and bugs are still being addressed, changes are expected to go through pull requests and issues, some automated tests but code coverage could be low, optional CI, the README is clear and minimally complete but might be lacking in extensive detail or examples, etc.

Development (Under Construction): The repository is undergoing initial development and is not ready to be used yet.
Not recommended for use outside of development environments.
The repository has some or all of the following attributes; the developer might be regularly commiting directly to the main branch, pull requests reviews are optional, no CI/CD, tests might not be passing, README might be sparse, etc.

Inactive or Stale: The repository has some or all of the following attributes; unresponsive maintainers, many unaddressed issues or pull requests, security patches are not kept up to date, unresolved failing CI pipelines, etc.

Unknown: The status of the connector is currently undefined.
We encourage community memebers to submit merge requests to update incorrect statuses.


## Connector Owners

Check out all the [published connectors](https://hub.meltano.com/singer/maintainers/meltanolabs) on MeltanoHub!

### Taps

| Connector Name                                                              | Status                           | Member/Organization Name                                                                                                 | MeltanoHub                                                         |
|-----------------------------------------------------------------------------|----------------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------|
| [tap-athena](https://github.com/MeltanoLabs/tap-athena)                     | Development (Under Construction) | [AJ Steers](https://github.com/aaronsteers) - Maintainer                     | [Link](https://hub.meltano.com/taps/athena--meltanolabs)           |
| [tap-circle-ci](https://github.com/MeltanoLabs/tap-circle-ci)                           | Prerelease (Beta)                | [Fran Lozano](https://github.com/franloza) - Maintainer                    | - |
| [tap-csv](https://github.com/MeltanoLabs/tap-csv)                           | Prerelease (Beta)                | [Pat Nadolny](https://github.com/pnadolny13) - Maintainer                    | [Link](https://hub.meltano.com/taps/csv--meltanolabs)              |
| [tap-dbt](https://github.com/MeltanoLabs/tap-dbt)                           | Active (Stable)                  | [Edgar Ramírez](https://github.com/edgarrmondragon) - Maintainer             | [Link](https://hub.meltano.com/taps/dbt--meltanolabs)              |
| [tap-github](https://github.com/MeltanoLabs/tap-github)                     | Active (Stable)                  | [Eric Boucher](https://github.com/ericboucher) - Maintainer                  | [Link](https://hub.meltano.com/taps/github-search--meltanolabs)    |
|                                                                             |                                  | [Laurent Savaete](https://github.com/laurentS)  - Maintainer                 |                                                                    |
| [tap-gitlab](https://github.com/MeltanoLabs/tap-gitlab)                     | Active (Stable)                  | 🔭 Looking For Maintainers! 🔭                                                | [Link](https://hub.meltano.com/taps/gitlab--meltanolabs)           |
| [tap-google-analytics](https://github.com/MeltanoLabs/tap-google-analytics) | Active (Stable)                  | [Pat Nadolny](https://github.com/pnadolny13) - Maintainer                    | [Link](https://hub.meltano.com/taps/google-analytics--meltanolabs) |
| [tap-peloton](https://github.com/MeltanoLabs/tap-peloton)                   | Prerelease (Beta)                | [Taylor Murphy](https://github.com/tayloramurphy) - Maintainer               | [Link](https://hub.meltano.com/taps/peloton--meltanolabs)          |
| [tap-slack](https://github.com/MeltanoLabs/tap-slack)                       | Active (Stable)                  | [Stephen Bailey](https://github.com/stkbailey) - Maintainer                  | -                                                                  |
| [tap-stackexchange](https://github.com/MeltanoLabs/tap-stackexchange)       | Active (Stable)                  | [Edgar Ramírez](https://github.com/edgarrmondragon) - Maintainer             | [Link](https://hub.meltano.com/taps/stackexchange--meltanolabs)    |
| [tap-sqlalchemy](https://github.com/MeltanoLabs/tap-sqlalchemy)             | Development (Under Construction) | [AJ Steers](https://github.com/aaronsteers) - Maintainer                     | -                                                                  |
| [tap-sftp](https://github.com/MeltanoLabs/tap-sftp)             | Active (Stable) | [Henning](https://github.com/radbrt) - Maintainer                     | [Link](https://hub.meltano.com/taps/sftp--meltanolabs) |

### Targets

| Connector Name                                                              | Status                           | Member/Organization Name                                                     | MeltanoHub                                                         |
|-----------------------------------------------------------------------------|----------------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------|
| [target-athena](https://github.com/MeltanoLabs/target-athena)               | Active (Stable)                  | [Andrew Stewart](https://github.com/andrewcstewart) - Maintainer             | [Link](https://hub.meltano.com/targets/athena--dataops-tk)         |
|                                                                             |                                  | [AJ Steers](https://github.com/aaronsteers) - Maintainer                     |                                                                    |
| [target-csv](https://github.com/MeltanoLabs/target-csv)                     | Prerelease (Beta)                | [AJ Steers](https://github.com/aaronsteers) - Maintainer                     | -                                                                  |
| [target-sqlite](https://github.com/MeltanoLabs/target-sqlite)               | Active (Stable)                  | 🔭 Looking For Maintainers! 🔭                                                | [Link](https://hub.meltano.com/targets/sqlite--meltanolabs)        |
| [target-postgres](https://github.com/MeltanoLabs/target-postgres)| Development (Under Construction)| 🔭 Looking For Maintainers! 🔭 | TBD |
| [target-yaml](https://github.com/MeltanoLabs/target-yaml)                   | Prerelease (Beta)                | 🔭 Looking For Maintainers! 🔭                    | [Link](https://hub.meltano.com/targets/yaml--meltanolabs)          |
