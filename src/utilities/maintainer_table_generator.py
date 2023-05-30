from pytablewriter import MarkdownTableWriter
from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True
yaml.default_flow_style = False

LOOKUPS = {
    "status": {
        "active": "Active (Stable)",
        "beta": "Prerelease (Beta)",
        "development": "Development (Under Construction)"
    }
}


def main():
    with open("src/connector_owners.yml", "r") as f:
        data = yaml.load(f)
        for connector_type in data:
            value_matrix = []
            for connector in data[connector_type]:
                owners = connector["owners"][0]                  
                value_matrix.append([
                    f"[{connector['name']}]({connector['repo']})",
                    LOOKUPS["status"][connector["status"]],
                    f"[{owners['name']}](https://github.com/{owners['github_username']}) - {owners['role']}",
                    f"[Link]({connector['hub_link']})",
                ])
                if len(connector["owners"]) > 1:
                    for owner in connector["owners"][1:]:
                        value_matrix.append([
                            "",
                            "",
                            f"[{owner['name']}](https://github.com/{owner['github_username']}) - {owner['role']}",
                            "",
                        ])
            # Adds two lines between tables
            print("")
            print("")
            writer = MarkdownTableWriter(
                table_name=connector_type.capitalize(),
                headers=["Connector Name", "Status", "Member/Organization Name", "MeltanoHub"],
                value_matrix=value_matrix,
            )
            writer.write_table()

if __name__ == "__main__":
    main()