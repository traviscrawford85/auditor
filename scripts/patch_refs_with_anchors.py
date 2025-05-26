# scripts/patch_refs_with_anchors.py
from pathlib import Path
import yaml
import re

# Constants
OPENAPI_DIR = Path("openapi")
COMPONENTS_DIR = OPENAPI_DIR / "components"
INPUT_SPEC = OPENAPI_DIR / "final.merged.yaml"
OUTPUT_SPEC = OPENAPI_DIR / "final.normalized.yaml"
SCHEMA_REF_PATTERN = re.compile(r"\.\/schemas\/([\w\-]+)\.yaml")

def normalize_refs_in_spec(data):
    def recurse(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == "$ref" and isinstance(v, str):
                    match = SCHEMA_REF_PATTERN.match(v)
                    if match:
                        schema_name = match.group(1)
                        obj[k] = f"components/schemas.yaml#/components/schemas/{schema_name}"
                else:
                    recurse(v)
        elif isinstance(obj, list):
            for item in obj:
                recurse(item)
    recurse(data)

def patch_refs_in_file(file_path):
    with open(file_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    def patch_refs(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == "$ref" and isinstance(v, str) and v.startswith("./components/"):
                    obj[k] = f"../components/{v.split('./components/')[1]}"
                else:
                    patch_refs(v)
        elif isinstance(obj, list):
            for item in obj:
                patch_refs(item)

    patch_refs(data)

    # Overwrite file safely
    with open(file_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, sort_keys=False)

def main():
    if INPUT_SPEC.exists():
        with INPUT_SPEC.open("r", encoding="utf-8") as f:
            spec = yaml.safe_load(f)
        normalize_refs_in_spec(spec)
        with OUTPUT_SPEC.open("w", encoding="utf-8") as f:
            yaml.safe_dump(spec, f, sort_keys=False)
        print(f"✅ Normalized spec written to {OUTPUT_SPEC}")

    path_files = list((OPENAPI_DIR / "paths").rglob("*.yaml"))
    for path_file in path_files:
        patch_refs_in_file(path_file)
        print(f"✅ Patched refs in {path_file}")

if __name__ == "__main__":
    main()
