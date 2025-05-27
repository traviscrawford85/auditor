# A script to validate the responses in openapi/components/responses against the OpenAPI spec.
"""
Validate each response in components/responses/*.yaml to ensure:
- It defines at least a description
- If it has content, it must include 'application/json' or other media types with valid schema refs
- No invalid fields or misplaced nesting
"""

import sys
from pathlib import Path

import yaml


def validate_response(resp_path):
    errors = []
    with open(resp_path, "r", encoding="utf-8") as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            errors.append(f"{resp_path}: YAML error: {e}")
            return errors

    if not isinstance(data, dict):
        errors.append(f"{resp_path}: Not a valid YAML mapping/object.")
        return errors

    # The file may be wrapped (e.g. 200_Ok: {...}) or flat
    if len(data) == 1 and next(iter(data)).startswith(("2", "3", "4", "5")):
        name, resp = next(iter(data.items()))
    else:
        name, resp = resp_path.stem, data

    if not isinstance(resp, dict):
        errors.append(f"{resp_path}: Response '{name}' is not a mapping/object.")
        return errors

    # Must have description
    if "description" not in resp or not isinstance(resp["description"], str):
        errors.append(f"{resp_path}: Response '{name}' missing or invalid 'description'.")

    # If content is present, check media types and schema
    if "content" in resp:
        if not isinstance(resp["content"], dict):
            errors.append(f"{resp_path}: Response '{name}' 'content' is not a mapping/object.")
        else:
            for media_type, media_obj in resp["content"].items():
                if not isinstance(media_obj, dict):
                    errors.append(f"{resp_path}: Media type '{media_type}' is not a mapping/object.")
                    continue
                schema = media_obj.get("schema")
                if not schema:
                    errors.append(f"{resp_path}: Media type '{media_type}' missing 'schema'.")
                    continue
                if not (isinstance(schema, dict) and ("$ref" in schema or "type" in schema)):
                    errors.append(f"{resp_path}: Media type '{media_type}' schema must have $ref or type.")

    # Check for misplaced fields
    allowed_fields = {"description", "headers", "content", "links"}
    for key in resp:
        if key not in allowed_fields:
            errors.append(f"{resp_path}: Response '{name}' has invalid field '{key}'.")

    return errors

def main():
    resp_dir = Path("openapi/components/responses")
    if not resp_dir.exists():
        print("❌ Directory openapi/components/responses not found.")
        sys.exit(1)

    errors = []
    for file in resp_dir.glob("*.yaml"):
        errors.extend(validate_response(file))

    if errors:
        print("❌ Validation errors in responses:")
        for err in errors:
            print("  -", err)
        sys.exit(1)
    else:
        print("✅ All responses are valid.")

if __name__ == "__main__":
    main()

