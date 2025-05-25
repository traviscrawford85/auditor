import os
import re
import yaml

OPENAPI_ROOT = "./openapi"
SCHEMA_DIR = os.path.join(OPENAPI_ROOT, "components", "schemas")
SCHEMA_LOG = "schema_rename_log.txt"
RESERVED_KEYS = {
    "type", "allOf", "anyOf", "oneOf", "not",
    "properties", "required", "description", "title",
    "enum", "items", "format", "default", "nullable"
}

def load_schema_files():
    files = {}
    for file in os.listdir(SCHEMA_DIR):
        if file.endswith(".yaml"):
            path = os.path.join(SCHEMA_DIR, file)
            with open(path, "r") as f:
                try:
                    content = yaml.safe_load(f)
                    if content:
                        files[path] = content
                except yaml.YAMLError:
                    pass
    return files

def pascal_case(name: str) -> str:
    return "".join(word.capitalize() for word in re.split(r'[\W_]+', name))

def rename_schemas(schemas):
    ref_map = {}
    log_entries = []
    for path, content in list(schemas.items()):
        for key in list(content.keys()):
            if key in RESERVED_KEYS:
                log_entries.append(f"SKIPPED RESERVED KEY: {key} | {path}")
                break
            if not key[0].isupper() or "_" in key:
                new_key = pascal_case(key)
                content[new_key] = content.pop(key)

                new_file = os.path.join(SCHEMA_DIR, f"{new_key}.yaml")
                os.rename(path, new_file)

                ref_map[f"#/components/schemas/{key}"] = f"#/components/schemas/{new_key}"
                schemas[new_file] = schemas.pop(path)
                log_entries.append(f"{key} → {new_key} | {path} → {new_file}")
                print(f"✅ Renamed {key} → {new_key} and {path} → {new_file}")
                break
    return schemas, ref_map, log_entries

def update_all_refs(schemas, ref_map):
    def update_node(node):
        if isinstance(node, dict):
            return {k: update_node(v) if k != "$ref" else ref_map.get(v, v) for k, v in node.items()}
        elif isinstance(node, list):
            return [update_node(i) for i in node]
        return node

    for path in schemas:
        schemas[path] = update_node(schemas[path])
    return schemas

def write_back(schemas):
    for path, content in schemas.items():
        with open(path, "w") as f:
            yaml.dump(content, f, sort_keys=False)

def write_schema_log(entries):
    with open(SCHEMA_LOG, "w") as log:
        log.write("Renamed Schemas:\n")
        for entry in entries:
            log.write(f"{entry}\n")

if __name__ == "__main__":
    schemas = load_schema_files()
    updated_schemas, ref_map, log_entries = rename_schemas(schemas)
    updated_schemas = update_all_refs(updated_schemas, ref_map)
    write_back(updated_schemas)
    write_schema_log(log_entries)
    print("📝 schema_rename_log.txt written with reserved keyword filtering.")
