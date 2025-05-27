"""
Validate openapi/components.yaml to ensure:
- It contains all four sections: schemas, parameters, responses, requestBodies
- Each reference under each section is valid and conforms to expected structure
- Catch missing or incorrectly merged definitions from per-file bundling
"""

import sys
from pathlib import Path

import yaml

REQUIRED_SECTIONS = ["schemas", "parameters", "responses", "requestBodies"]

def validate_components(components):
    errors = []
    # Check for required sections
    for section in REQUIRED_SECTIONS:
        if section not in components:
            errors.append(f"Missing section: '{section}'")
            continue
        if not isinstance(components[section], dict):
            errors.append(f"Section '{section}' is not a mapping/object.")
            continue
        # Check each definition in the section
        for name, definition in components[section].items():
            if not isinstance(definition, dict):
                errors.append(f"{section}.{name} is not a mapping/object.")
                continue
            # Minimal structure checks
            if section == "schemas":
                if "type" not in definition:
                    errors.append(f"schemas.{name} missing 'type'.")
            elif section == "parameters":
                for field in ["name", "in", "schema"]:
                    if field not in definition:
                        errors.append(f"parameters.{name} missing '{field}'.")
            elif section == "responses":
                if "description" not in definition:
                    errors.append(f"responses.{name} missing 'description'.")
            elif section == "requestBodies":
                if "content" not in definition:
                    errors.append(f"requestBodies.{name} missing 'content'.")
    return errors

def main():
    comp_path = Path("openapi/components.yaml")
    if not comp_path.exists():
        print("❌ openapi/components.yaml not found.")
        sys.exit(1)

    with comp_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if "components" not in data or not isinstance(data["components"], dict):
        print("❌ No 'components' section found or invalid structure.")
        sys.exit(1)

    errors = validate_components(data["components"])
    if errors:
        print("❌ Validation errors in components.yaml:")
        for err in errors:
            print("  -", err)
        sys.exit(1)
    else:
        print("✅ components.yaml is valid.")

if __name__ == "__main__":
    main()
