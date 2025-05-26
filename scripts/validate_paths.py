"""
Validate each file in openapi/paths/*.yaml to ensure:
- It is wrapped in a top-level endpoint path (e.g. '/activities/{id}:')
- Each method (get, post, etc.) has 'operationId', 'tags', and 'responses'
- Each method's parameters and requestBody (if present) are valid
"""

import sys
import yaml
from pathlib import Path

VALID_METHODS = {"get", "post", "put", "patch", "delete", "options", "head"}

def validate_parameters(params, path_file, method, endpoint):
    errors = []
    if not isinstance(params, list):
        errors.append(f"{path_file}: {endpoint} {method} 'parameters' is not a list.")
        return errors
    for idx, param in enumerate(params):
        if not isinstance(param, dict):
            errors.append(f"{path_file}: {endpoint} {method} parameter at index {idx} is not a dict.")
            continue
        if "$ref" in param:
            continue  # Assume $ref is valid, deeper validation can be added
        for field in ["name", "in", "schema"]:
            if field not in param:
                errors.append(f"{path_file}: {endpoint} {method} parameter at index {idx} missing '{field}'.")
    return errors

def validate_request_body(request_body, path_file, method, endpoint):
    errors = []
    if not isinstance(request_body, dict):
        errors.append(f"{path_file}: {endpoint} {method} 'requestBody' is not a dict.")
        return errors
    if "$ref" in request_body:
        return errors  # Assume $ref is valid
    if "content" not in request_body or not isinstance(request_body["content"], dict):
        errors.append(f"{path_file}: {endpoint} {method} requestBody missing or invalid 'content'.")
    return errors

def validate_path_file(path_file):
    errors = []
    with open(path_file, "r", encoding="utf-8") as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            errors.append(f"{path_file}: YAML error: {e}")
            return errors

    if not isinstance(data, dict) or not data:
        errors.append(f"{path_file}: File is empty or not a mapping/object.")
        return errors

    for endpoint, methods in data.items():
        if not endpoint.startswith("/"):
            errors.append(f"{path_file}: Top-level key '{endpoint}' does not start with '/'.")
        if not isinstance(methods, dict):
            errors.append(f"{path_file}: Endpoint '{endpoint}' value is not a mapping/object.")
            continue
        for method, details in methods.items():
            if method not in VALID_METHODS:
                continue  # skip non-method keys
            if not isinstance(details, dict):
                errors.append(f"{path_file}: {endpoint} {method} is not a mapping/object.")
                continue
            # Required fields
            for field in ["operationId", "tags", "responses"]:
                if field not in details:
                    errors.append(f"{path_file}: {endpoint} {method} missing '{field}'.")
            # Validate parameters
            if "parameters" in details:
                errors.extend(validate_parameters(details["parameters"], path_file, method, endpoint))
            # Validate requestBody
            if "requestBody" in details:
                errors.extend(validate_request_body(details["requestBody"], path_file, method, endpoint))
    return errors

def main():
    paths_dir = Path("openapi/paths")
    if not paths_dir.exists():
        print("❌ Directory openapi/paths not found.")
        sys.exit(1)

    errors = []
    for file in paths_dir.glob("*.yaml"):
        errors.extend(validate_path_file(file))

    if errors:
        print("❌ Validation errors in paths:")
        for err in errors:
            print("  -", err)
        sys.exit(1)
    else:
        print("✅ All path files are valid.")

if __name__ == "__main__":
    main()

