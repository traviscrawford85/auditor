"""
Validate openapi/components/requestBodies.yaml after bundling to ensure:
- Each request body includes a 'content' section with proper media type(s)
- Each media type includes a valid schema reference or inline schema
- Detect duplicate or invalid definitions introduced during bundling
"""

import sys
from pathlib import Path

import yaml


def validate_request_bodies(request_bodies):
    errors = []
    seen = set()
    for name, body in request_bodies.items():
        # Check for duplicates
        if name in seen:
            errors.append(f"Duplicate request body: {name}")
            continue
        seen.add(name)

        # Must have 'content'
        if "content" not in body or not isinstance(body["content"], dict):
            errors.append(f"Request body '{name}' missing or invalid 'content' section.")
            continue

        # Each media type must have a schema or $ref
        for media_type, media_obj in body["content"].items():
            if not isinstance(media_obj, dict):
                errors.append(f"Request body '{name}' media type '{media_type}' is not a dict.")
                continue
            schema = media_obj.get("schema")
            if not schema:
                errors.append(f"Request body '{name}' media type '{media_type}' missing 'schema'.")
                continue
            if not (isinstance(schema, dict) and ("$ref" in schema or "type" in schema)):
                errors.append(f"Request body '{name}' media type '{media_type}' schema must have $ref or type.")

    return errors

def main():
    reqbods_path = Path("openapi/components/requestBodies.yaml")
    if not reqbods_path.exists():
        print("❌ openapi/requestBodies.yaml not found.")
        sys.exit(1)

    with reqbods_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    # Support both wrapped and flat styles
    if "components" in data and "requestBodies" in data["components"]:
        request_bodies = data["components"]["requestBodies"]
    elif "requestBodies" in data:
        request_bodies = data["requestBodies"]
    else:
        request_bodies = data

    if not isinstance(request_bodies, dict):
        print("❌ No request bodies found or invalid structure.")
        sys.exit(1)

    errors = validate_request_bodies(request_bodies)
    if errors:
        print("❌ Validation errors in requestBodies.yaml:")
        for err in errors:
            print("  -", err)
        sys.exit(1)
    else:
        print("✅ All request bodies are valid.")

if __name__ == "__main__":
    main()
