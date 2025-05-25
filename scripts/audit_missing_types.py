import os
import yaml

SCHEMA_PATH = "./openapi/components/schemas"
MISSING_TYPE_LOG = "missing_schema_property_types.txt"
missing_entries = []

def audit_missing_types():
    for file in os.listdir(SCHEMA_PATH):
        if file.endswith(".yaml"):
            path = os.path.join(SCHEMA_PATH, file)
            with open(path, "r") as f:
                schema = yaml.safe_load(f)
                if not schema or not isinstance(schema, dict):
                    continue
                key = list(schema.keys())[0]
                data = schema[key]
                if not isinstance(data, dict) or "properties" not in data:
                    continue
                for prop_name, prop_value in data.get("properties", {}).items():
                    if isinstance(prop_value, dict) and "type" not in prop_value and "$ref" not in prop_value:
                        missing_entries.append(f"{file}: property '{prop_name}' missing type")

    with open(MISSING_TYPE_LOG, "w") as log_file:
        log_file.write("Properties missing 'type':\n")
        for entry in missing_entries:
            log_file.write(entry + "\n")

if __name__ == "__main__":
    audit_missing_types()
    print("✅ Audit complete. See missing_schema_property_types.txt.")
