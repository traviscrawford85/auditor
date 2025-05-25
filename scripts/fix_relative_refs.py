import os
import yaml

OPENAPI_DIR = "./openapi"
TARGET_FOLDER = "components"

def fix_refs_in_file(filepath):
    changed = False

    def fix_ref_path(ref, current_file):
        if isinstance(ref, str) and TARGET_FOLDER in ref and not ref.startswith("../"):
            base_path = os.path.dirname(current_file)
            while not os.path.isdir(os.path.join(base_path, TARGET_FOLDER)):
                base_path = os.path.dirname(base_path)
                if base_path == "/":
                    break
            rel_path = os.path.relpath(os.path.join(base_path, TARGET_FOLDER), os.path.dirname(current_file))
            return ref.replace(f"{TARGET_FOLDER}/", f"{rel_path}/{TARGET_FOLDER}/")
        return ref

    def recurse(obj, current_file):
        nonlocal changed
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == "$ref":
                    fixed = fix_ref_path(v, current_file)
                    if fixed != v:
                        obj[k] = fixed
                        changed = True
                else:
                    recurse(v, current_file)
        elif isinstance(obj, list):
            for item in obj:
                recurse(item, current_file)

    with open(filepath, "r") as f:
        content = yaml.safe_load(f)

    if content:
        recurse(content, filepath)

    if changed:
        with open(filepath, "w") as f:
            yaml.dump(content, f, sort_keys=False)
        print(f"✅ Fixed refs in: {filepath}")

def walk_and_fix():
    for subdir, _, files in os.walk(OPENAPI_DIR):
        for file in files:
            if file.endswith((".yaml", ".yml")):
                fix_refs_in_file(os.path.join(subdir, file))

if __name__ == "__main__":
    walk_and_fix()
