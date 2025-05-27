import os
import re

import yaml

OPENAPI_ROOT = "./openapi"
ALLOWED_ENTITIES = {
    "matters", "contacts", "tasks", "calendars", "activities",
    "documents", "notes", "custom_fields", "custom_field_values",
    "custom_actions", "practice_areas", "users", "relationships"
}

def load_yaml_files():
    schemas = {}
    for subdir, _, files in os.walk(OPENAPI_ROOT):
        for file in files:
            if file.endswith((".yaml", ".yml")):
                path = os.path.join(subdir, file)
                with open(path, "r") as f:
                    try:
                        content = yaml.safe_load(f)
                        if content:
                            schemas[path] = content
                    except yaml.YAMLError:
                        pass
    return schemas

def normalize_operation_id(route, method, used_ids):
    parts = route.strip("/").split("/")
    parts = [p for p in parts if not p.startswith("{")]
    base = "_".join(parts).replace("-", "_")
    op_id = f"{method}_{base}"
    suffix = 1
    while op_id in used_ids:
        op_id = f"{method}_{base}_{suffix}"
        suffix += 1
    used_ids.add(op_id)
    return op_id

def inject_path_params(route):
    return [
        {
            "name": match,
            "in": "path",
            "required": True,
            "schema": {"type": "string"}
        }
        for match in re.findall(r"{([^}]+)}", route)
    ]

def process_schemas(schemas):
    updated_schemas = {}
    used_ids = set()
    for path, content in schemas.items():
        new_paths = {}
        for route, methods in content.get("paths", {}).items():
            if any(entity in route for entity in ALLOWED_ENTITIES):
                new_methods = {}
                for method, op in methods.items():
                    if isinstance(op, dict):
                        op = op.copy()
                        op["operationId"] = normalize_operation_id(route, method, used_ids)
                        if "requestBody" in op:
                            entity = route.strip("/").split("/")[0]
                            op["requestBody"] = {"$ref": f"#/components/requestBodies/{entity.capitalize()}{method.capitalize()}Request"}
                        if "parameters" not in op:
                            op["parameters"] = []
                        existing_params = {param["name"] for param in op["parameters"] if isinstance(param, dict)}
                        for param in inject_path_params(route):
                            if param["name"] not in existing_params:
                                op["parameters"].append(param)
                        new_methods[method] = op
                    else:
                        print(f"[WARNING] Skipped non-dict operation in {path} at {route} → {method}")
                if new_methods:
                    new_paths[route] = new_methods
        if new_paths:
            content["paths"] = new_paths
            updated_schemas[path] = content
    return updated_schemas

def write_back(schemas):
    for path, content in schemas.items():
        with open(path, "w") as f:
            yaml.dump(content, f, sort_keys=False)

if __name__ == "__main__":
    schemas = load_yaml_files()
    updated = process_schemas(schemas)
    write_back(updated)
    print("Normalized operationIds and injected missing path parameters.")
