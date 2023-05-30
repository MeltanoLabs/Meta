# Contributing


### README Connector Owners Regenerate

The connector owners for MeltanoLabs can be managed using the `src/connector_owneres.yml` file.
When the file is updated it can be used to auto generate the README tables.

1. Install dependencies

poetry install

2. Run generator script

poetry run python src/utilities/maintainer_table_generator.py

3. Copy outputs into README.
