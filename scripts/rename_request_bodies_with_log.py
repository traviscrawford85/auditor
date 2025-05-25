import os
import re
import yaml
from shutil import move

OPENAPI_ROOT = "./openapi"
LOG_FILE = "rename_log.txt"

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
    log_entries = []
    skipped = []

    for path, content in list(schemas.items()):
        if "requestBodies" not in path:
            continue

        filename = os.path.basename(path).split(".")[0]
        new_key = None
        current_key = None

        if isinstance(content, dict) and len(content) == 1:
            current_key, val = next(iter(content.items()))
            desc = val.get("description", "")
            match = re.search(r"Request Body for ([A-Za-z0-9_]+)", str(desc))
            if match:
                new_key = f"{match.group(1)}Request"
                content[new_key] = content.pop(current_key)
        elif isinstance(content, dict):
            desc = content.get("description", "")
            match = re.search(r"Request Body for ([A-Za-z0-9_]+)", str(desc))
            if match:
                new_key = f"{match.group(1)}Request"
                content = {new_key: content}
                current_key = filename
            else:
                skipped.append(f"{path} (no match in flat format: {desc})")
                continue
        else:
            skipped.append(f"{path} (not a dict structure)")
            continue

        if new_key:
            new_path = os.path.join(os.path.dirname(path), f"{new_key}.yaml")
            move(path, new_path)
            schemas[new_path] = content
            schemas.pop(path, None)
            ref_map[f"#/{current_key}"] = f"#/{new_key}"
            log_entries.append(f"{current_key} → {new_key} | {path} → {new_path}")
            print(f"✅ Renamed {current_key} → {new_key} and {path} → {new_path}")

    return schemas, ref_map, log_entries, skipped

def update_refs(schemas, ref_map):
    def update_node(node):
        if isinstance(node, dict):
            return {k: update_node(v) if k != "$ref" else ref_map.get(v, v) for k, v in node.items()}
        elif isinstance(node, list):
            return [update_node(i) for i in node]
        return node

    for path in schemas:
        schemas[path] = update_node(schemas[path])
    return schemas

def write_back(schemas):
    for path, content in schemas.items():
        with open(path, "w") as f:
            yaml.dump(content, f, sort_keys=False)

def write_log(success, skipped):
    with open(LOG_FILE, "w") as log:
        log.write("Renamed Request Bodies:\n")
        for entry in success:
            log.write(f"{entry}\n")
        log.write("\nSkipped (reason):\n")
        for entry in skipped:
            log.write(f"{entry}\n")

if __name__ == "__main__":
    schemas = load_yaml_files()
    updated_schemas, ref_map, log_entries, skipped_entries = rename_request_bodies(schemas)
    updated_schemas = update_refs(updated_schemas, ref_map)
    write_back(updated_schemas)
    write_log(log_entries, skipped_entries)
    print("📝 rename_log.txt written.")
