# A script to validate the schemas in openapi/components/schemas against the OpenAPI spec.
"""
Validate each schema in components/schemas/*.yaml to ensure:
- It defines a top-level object with required 'type' field (usually 'object')
- It includes properties or items if appropriate
- There are no invalid fields or misplaced definitions
"""

import sys
from pathlib import Path

import yaml


def validate_schema(schema_path):
    errors = []
    with open(schema_path, "r", encoding="utf-8") as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            errors.append(f"{schema_path}: YAML error: {e}")
            return errors

    if not isinstance(data, dict):
        errors.append(f"{schema_path}: Not a valid YAML mapping/object.")
        return errors

    # The file may be wrapped (e.g. MySchema: {...}) or flat
    if len(data) == 1 and isinstance(next(iter(data.values())), dict):
        name, schema = next(iter(data.items()))
    else:
        name, schema = schema_path.stem, data

    if not isinstance(schema, dict):
        errors.append(f"{schema_path}: Schema '{name}' is not a mapping/object.")
        return errors

    # Must have 'type'
    if "type" not in schema:
        errors.append(f"{schema_path}: Schema '{name}' missing required 'type' field.")
    else:
        # If type is object, should have properties or additionalProperties
        if schema["type"] == "object":
            if "properties" not in schema and "additionalProperties" not in schema:
                errors.append(f"{schema_path}: Schema '{name}' of type 'object' missing 'properties' or 'additionalProperties'.")
        # If type is array, should have items
        if schema["type"] == "array" and "items" not in schema:
            errors.append(f"{schema_path}: Schema '{name}' of type 'array' missing 'items'.")

    # Check for misplaced fields (optional, can be expanded)
    allowed_fields = {
        "type", "properties", "items", "required", "description", "enum", "format",
        "additionalProperties", "allOf", "anyOf", "oneOf", "title", "default", "example", "nullable", "readOnly", "writeOnly", "deprecated", "discriminator", "xml", "externalDocs"
    }
    for key in schema:
        if key not in allowed_fields:
            errors.append(f"{schema_path}: Schema '{name}' has invalid or misplaced field '{key}'.")

    return errors

def main():
    schemas_dir = Path("openapi/components/schemas")
    if not schemas_dir.exists():
        print("❌ Directory openapi/components/schemas not found.")
        sys.exit(1)

    errors = []
    for file in schemas_dir.glob("*.yaml"):
        errors.extend(validate_schema(file))

    if errors:
        print("❌ Validation errors in schemas:")
        for err in errors:
            print("  -", err)
        sys.exit(1)
    else:
        print("✅ All schemas are valid.")

if __name__ == "__main__":
    main()

