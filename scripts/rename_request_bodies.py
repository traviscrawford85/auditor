import os
import yaml
import re

OPENAPI_ROOT = "./openapi"

def load_yaml_files():
    files = {}
    for subdir, _, filelist in os.walk(OPENAPI_ROOT):
        for file in filelist:
            if file.endswith((".yaml", ".yml")):
                path = os.path.join(subdir, file)
                with open(path, "r") as f:
                    try:
                        content = yaml.safe_load(f)
                        if content:
                            files[path] = content
                    except yaml.YAMLError:
                        pass
    return files

def rename_request_bodies(schemas):
    ref_map = {}

    for path, content in schemas.items():
        request_bodies = content.get("components", {}).get("requestBodies", {})
        new_bodies = {}
        changed = False

        for key, value in request_bodies.items():
            if re.match(r"^ReqBody_", key) and "description" in value:
                match = re.search(r"Request Body for (\w+)", value["description"])
                if match:
                    new_key = f"{match.group(1)}Request"
                    ref_map[f"#/components/requestBodies/{key}"] = f"#/components/requestBodies/{new_key}"
                    new_bodies[new_key] = value
                    changed = True
                else:
                    new_bodies[key] = value
            else:
                new_bodies[key] = value

        if changed:
            content["components"]["requestBodies"] = new_bodies
            schemas[path] = content

    return schemas, ref_map

def update_refs(schemas, ref_map):
    def update_node(node):
        if isinstance(node, dict):
            return {
                k: update_refs(v, ref_map) if k != "$ref" else ref_map.get(v, v)
                for k, v in node.items()
            }
        elif isinstance(node, list):
            return [update_refs(i, ref_map) for i in node]
        else:
            return node

    for path in schemas:
        schemas[path] = update_node(schemas[path])

    return schemas

def write_back(schemas):
    for path, content in schemas.items():
        with open(path, "w") as f:
            yaml.dump(content, f, sort_keys=False)

if __name__ == "__main__":
    schemas = load_yaml_files()
    updated_schemas, ref_map = rename_request_bodies(schemas)
    updated_schemas = update_refs(updated_schemas, ref_map)
    write_back(updated_schemas)
    print("Request body names and refs updated successfully.")
