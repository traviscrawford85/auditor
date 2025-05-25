import os
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

def normalize_operation_id(route, method):
    parts = route.strip("/").split("/")
    parts = [p for p in parts if not p.startswith("{")]
    base = "_".join(parts)
    return f"{method}_{base}".replace("-", "_")

def rename_request_body(entity, method):
    return f"#/components/requestBodies/{entity.capitalize()}{method.capitalize()}Request"

def process_schemas(schemas):
    updated_schemas = {}
    for path, content in schemas.items():
        new_paths = {}
        for route, methods in content.get("paths", {}).items():
            if any(entity in route for entity in ALLOWED_ENTITIES):
                new_methods = {}
                for method, op in methods.items():
                    op["operationId"] = normalize_operation_id(route, method)
                    if "requestBody" in op:
                        entity = route.split("/")[1]
                        op["requestBody"] = {"$ref": rename_request_body(entity, method)}
                    new_methods[method] = op
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
    filtered = process_schemas(schemas)
    write_back(filtered)
