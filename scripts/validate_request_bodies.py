# A script to validate the request bodies in openapi/components/requestBodies against the OpenAPI spec.
"""
Validate each request body in components/requestBodies/*.yaml to ensure:
- It defines 'content' with media type(s), typically 'application/json'
- Each media type must include a valid schema or schema $ref
- Optional 'description' and 'required' fields are valid if present
- Flags any request bodies missing `content`, `schema`, or `description`.
"""

import sys
from pathlib import Path

import yaml


def validate_request_body(rb_path):
    errors = []
    with open(rb_path, "r", encoding="utf-8") as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            errors.append(f"{rb_path}: YAML error: {e}")
            return errors

    if not isinstance(data, dict):
        errors.append(f"{rb_path}: Not a valid YAML mapping/object.")
        return errors

    # The file may be wrapped (components/requestBodies/ReqBodyName: {...}) or flat
    if len(data) == 1 and next(iter(data)).startswith("ReqBody"):
        # Wrapped style
        name, body = next(iter(data.items()))
    else:
        # Flat style
        name, body = rb_path.stem, data

    if not isinstance(body, dict):
        errors.append(f"{rb_path}: Request body '{name}' is not a mapping/object.")
        return errors

    # Check for content
    if "content" not in body or not isinstance(body["content"], dict):
        errors.append(f"{rb_path}: Request body '{name}' missing or invalid 'content' section.")
        return errors

    # Check each media type
    for media_type, media_obj in body["content"].items():
        if not isinstance(media_obj, dict):
            errors.append(f"{rb_path}: Media type '{media_type}' is not a mapping/object.")
            continue
        schema = media_obj.get("schema")
        if not schema:
            errors.append(f"{rb_path}: Media type '{media_type}' missing 'schema'.")
            continue
        if not (isinstance(schema, dict) and ("$ref" in schema or "type" in schema)):
            errors.append(f"{rb_path}: Media type '{media_type}' schema must have $ref or type.")

    # Optional: check description and required fields
    if "description" in body and not isinstance(body["description"], str):
        errors.append(f"{rb_path}: 'description' should be a string.")
    if "required" in body and not isinstance(body["required"], bool):
        errors.append(f"{rb_path}: 'required' should be a boolean.")

    return errors

def main():
    reqbods_dir = Path("openapi/components/requestBodies")
    if not reqbods_dir.exists():
        print("❌ Directory openapi/components/requestBodies not found.")
        sys.exit(1)

    errors = []
    for file in reqbods_dir.glob("*.yaml"):
        errors.extend(validate_request_body(file))

    if errors:
        print("❌ Validation errors in requestBodies:")
        for err in errors:
            print("  -", err)
        sys.exit(1)
    else:
        print("✅ All request bodies are valid.")

if __name__ == "__main__":
    main()
