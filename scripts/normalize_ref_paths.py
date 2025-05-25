import os
import yaml
import re

OPENAPI_ROOT = "./openapi"
REPEATED = re.compile(r"(components/)+")

def normalize_ref_path(ref):
    if isinstance(ref, str) and "components/" in ref:
        fixed = REPEATED.sub("components/", ref)
        return fixed
    return ref

def fix_refs_in_file(filepath):
    changed = False

    def recurse(obj):
        nonlocal changed
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == "$ref" and isinstance(v, str):
                    fixed = normalize_ref_path(v)
                    if fixed != v:
                        obj[k] = fixed
                        changed = True
                else:
                    recurse(v)
        elif isinstance(obj, list):
            for item in obj:
                recurse(item)

    with open(filepath, "r") as f:
        content = yaml.safe_load(f)

    if content:
        recurse(content)

    if changed:
        with open(filepath, "w") as f:
            yaml.dump(content, f, sort_keys=False)
        print(f"✅ Normalized $ref paths in: {filepath}")

def walk_openapi_files():
    for subdir, _, files in os.walk(OPENAPI_ROOT):
        for file in files:
            if file.endswith((".yaml", ".yml")):
                fix_refs_in_file(os.path.join(subdir, file))

if __name__ == "__main__":
    walk_openapi_files()
