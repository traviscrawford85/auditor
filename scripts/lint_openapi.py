import os
from collections import defaultdict

import yaml

OPENAPI_ROOT = "./openapi"


def load_yaml_files():
    schemas = {}
    for subdir, _, files in os.walk(OPENAPI_ROOT):
        for file in files:
            if file.endswith((".yaml", ".yml")):
                path = os.path.join(subdir, file)
                with open(path, "r") as f:
                    try:
                        content = yaml.safe_load(f)
                        if content:
                            schemas[path] = content
                    except yaml.YAMLError:
                        pass
    return schemas


def collect_refs(schema):
    refs = set()

    def recurse(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if k == "$ref":
                    refs.add(v)
                recurse(v)
        elif isinstance(node, list):
            for i in node:
                recurse(i)

    recurse(schema)
    return refs


def find_unused_components(schemas):
    used_refs = set()
    for schema in schemas.values():
        used_refs.update(collect_refs(schema))

    unused = defaultdict(list)
    for path, content in schemas.items():
        components = content.get("components", {})
        for section, items in components.items():
            for name in items:
                ref = f"#/components/{section}/{name}"
                if ref not in used_refs:
                    unused[path].append(ref)
    return unused


if __name__ == "__main__":
    schemas = load_yaml_files()
    unused = find_unused_components(schemas)
    for path, refs in unused.items():
        print(f"{path}:")
        for ref in refs:
            print(f"  - {ref}")
