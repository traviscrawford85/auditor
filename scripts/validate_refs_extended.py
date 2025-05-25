import os
import yaml

OPENAPI_ROOT = "./openapi"

def load_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def collect_refs(schema, current_file):
    refs = []

    def recurse(obj, path="root"):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == "$ref":
                    refs.append((v, path, current_file))
                else:
                    recurse(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                recurse(item, f"{path}[{i}]")

    recurse(schema)
    return refs

def resolve_internal_ref(ref, schema, source_file, location):
    parts = ref.strip("#/").split("/")
    ref_obj = schema
    try:
        for part in parts:
            ref_obj = ref_obj[part]
    except (KeyError, TypeError):
        print(f"[ERROR] Broken internal ref in {source_file} at {location}: {ref}")

def resolve_external_ref(ref, base_dir, source_file, location):
    if "#" not in ref:
        print(f"[WARNING] External ref missing anchor in {source_file} at {location}: {ref}")
        return
    file_part, anchor = ref.split("#", 1)
    full_path = os.path.normpath(os.path.join(base_dir, file_part))
    if not os.path.isfile(full_path):
        print(f"[ERROR] Missing file for external ref in {source_file} at {location}: {ref}")
        return
    try:
        target_schema = load_yaml(full_path)
        resolve_internal_ref("#/" + anchor.strip("/"), target_schema, full_path, location)
    except Exception as e:
        print(f"[ERROR] Failed to load or parse {full_path}: {e}")

def validate_all_refs(base_path):
    for subdir, _, files in os.walk(base_path):
        for file in files:
            if file.endswith((".yaml", ".yml")):
                full_path = os.path.join(subdir, file)
                try:
                    schema = load_yaml(full_path)
                    refs = collect_refs(schema, full_path)
                    for ref, location, source_file in refs:
                        if ref.startswith("#/"):
                            resolve_internal_ref(ref, schema, source_file, location)
                        elif ref.endswith(".yaml") or ref.endswith(".yml") or ref.startswith("./"):
                            resolve_external_ref(ref, os.path.dirname(source_file), source_file, location)
                        else:
                            print(f"[WARNING] Unknown $ref format in {source_file} at {location}: {ref}")
                except yaml.YAMLError as e:
                    print(f"[ERROR] YAML parse error in {full_path}: {e}")

if __name__ == "__main__":
    validate_all_refs(OPENAPI_ROOT)
