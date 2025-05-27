import os
import re
from pathlib import Path

import yaml

BASE_DIR = Path("openapi")
SCHEMA_REF_PATTERN = re.compile(r"\.\/schemas\/([\w\-]+)\.yaml")

def normalize_refs_in_file(file_path: Path):
    changed = False

    def recurse(obj):
        nonlocal changed
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == "$ref" and isinstance(v, str):
                    match = SCHEMA_REF_PATTERN.match(v)
                    if match:
                        schema_name = match.group(1)
                        new_ref = f"components/schemas.yaml#/components/schemas/{schema_name}"
                        obj[k] = new_ref
                        changed = True
                else:
                    recurse(v)
        elif isinstance(obj, list):
            for item in obj:
                recurse(item)

    with open(file_path, "r", encoding="utf-8") as f:
        try:
            content = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"❌ Skipping {file_path}: {e}")
            return

    if content:
        recurse(content)

    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(content, f, sort_keys=False)
        print(f"✅ Rewritten refs in: {file_path}")

def main():
    for root, _, files in os.walk(BASE_DIR):
        for name in files:
            if name.endswith(".yaml") or name.endswith(".yml"):
                normalize_refs_in_file(Path(root) / name)

if __name__ == "__main__":
    main()
