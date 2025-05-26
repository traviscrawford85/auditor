import os
import yaml
from pathlib import Path

REQUIRED_PATH_KEYS = {"get", "post", "put", "patch", "delete"}
REQUIRED_COMPONENT_KEYS = {
    "parameters": ["name", "in", "schema"],
    "requestBodies": ["content"],
    "responses": ["description"],
    "schemas": ["type"]
}

BASE_DIR = Path("openapi")


def validate_yaml_file(path, validators):
    errors = []
    with open(path, "r", encoding="utf-8") as f:
        try:
            content = yaml.safe_load(f)
        except yaml.YAMLError as e:
            return [f"YAML error in {path}: {e}"]

    if not content:
        return [f"Empty or invalid YAML in {path}"]

    for validator in validators:
        result = validator(content, path)
        if result:
            errors.extend(result)
    return errors


def validate_paths(content, path):
    if not any(k in content for k in REQUIRED_PATH_KEYS):
        return [f"Missing HTTP method (get, post, etc.) in path: {path}"]
    return []


def validate_components(section, required_keys):
    def inner(content, path):
        section_data = content.get("components", {}).get(section, {})
        if not isinstance(section_data, dict):
            return [f"Missing or invalid section '{section}' in {path}"]
        errors = []
        for name, definition in section_data.items():
            for key in required_keys:
                if key not in definition:
                    errors.append(f"Missing '{key}' in {section}/{name} from {path}")
        return errors

    return inner


def audit_all():
    all_errors = []
    # Paths
    for file in (BASE_DIR / "paths").rglob("*.yaml"):
        errors = validate_yaml_file(file, [validate_paths])
        all_errors.extend(errors)

    # Components
    for section, keys in REQUIRED_COMPONENT_KEYS.items():
        for file in (BASE_DIR / "components" / section).rglob("*.yaml"):
            errors = validate_yaml_file(file, [validate_components(section, keys)])
            all_errors.extend(errors)

    if all_errors:
        print("\n\n🔍 Audit Errors Found:")
        for err in all_errors:
            print(f"❌ {err}")
    else:
        print("✅ All components and paths passed validation!")


if __name__ == "__main__":
    audit_all()
