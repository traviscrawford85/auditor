import os

import yaml

OPENAPI_DIR = "./openapi"
TARGET_FOLDER = "components"

def fix_refs_in_file(filepath):
    changed = False

    def fix_ref_path(ref):
        if isinstance(ref, str) and "#/components/" in ref:
            parts = ref.split("#/")
            path = parts[0].replace("..", "").replace("./", "").replace("//", "/").strip("/")
            fragment = parts[1].split("/")
            if len(fragment) >= 3:
                component_type = fragment[1]
                component_name = fragment[2]
                new_ref = f"components/{component_type}.yaml#/components/{component_type}/{component_name}"
                return new_ref
        return ref


    def recurse(obj, current_file):
        nonlocal changed
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == "$ref":
                    fixed = fix_ref_path(v)
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
