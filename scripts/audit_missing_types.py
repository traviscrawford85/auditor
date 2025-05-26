import os
import yaml
from pathlib import Path

SCHEMA_PATH = Path("./openapi/components/schemas")
MISSING_TYPE_LOG = "missing_schema_property_types.txt"
missing_entries = []

def audit_missing_types():
    for file in SCHEMA_PATH.glob("*.yaml"):
        with open(file, "r", encoding="utf-8") as f:
            schema = yaml.safe_load(f)
            if not schema or not isinstance(schema, dict):
                continue

            # Support both single-level and named schema wrapping
            top_level = list(schema.values())[0] if list(schema.keys())[0] != "type" else schema

            if not isinstance(top_level, dict):
                continue

            props = top_level.get("properties", {})
            if not isinstance(props, dict):
                continue

            for prop, val in props.items():
                if isinstance(val, dict) and "type" not in val and "$ref" not in val:
                    missing_entries.append(f"{file.name}: property '{prop}' missing type")

    with open(MISSING_TYPE_LOG, "w", encoding="utf-8") as log_file:
        log_file.write("Properties missing 'type':\n")
        for entry in missing_entries:
            log_file.write(entry + "\n")

if __name__ == "__main__":
    audit_missing_types()
    print("✅ Audit complete. See missing_schema_property_types.txt.")
