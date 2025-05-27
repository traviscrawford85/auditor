import os
import re
from collections import defaultdict

import yaml

ROOT_PATH = "./openapi/root.yaml"

def extract_prefix(tag_name):
    match = re.match(r"([A-Za-z]+)", tag_name)
    return match.group(1) if match else "Other"

def group_tags_by_prefix(tags):
    groups = defaultdict(list)
    for tag in tags:
        name = tag.get("name")
        if name:
            prefix = extract_prefix(name)
            groups[prefix].append(name)
    return [{"name": prefix, "tags": sorted(set(names))} for prefix, names in sorted(groups.items())]

def add_x_tagGroups():
    if not os.path.exists(ROOT_PATH):
        print("❌ root.yaml not found.")
        return

    with open(ROOT_PATH, "r") as f:
        spec = yaml.safe_load(f)

    tags = spec.get("tags", [])
    if not tags:
        print("ℹ️ No tags defined in root.yaml.")
        return

    tag_groups = group_tags_by_prefix(tags)
    spec["x-tagGroups"] = tag_groups

    with open(ROOT_PATH, "w") as f:
        yaml.dump(spec, f, sort_keys=False)

    print("✅ x-tagGroups generated and added to root.yaml.")

if __name__ == "__main__":
    add_x_tagGroups()
