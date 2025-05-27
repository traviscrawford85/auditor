import os
import re
from pathlib import Path

import yaml

REQUEST_BODIES_DIR = Path("openapi/components/requestBodies")
REQUEST_BODIES_BUNDLE = Path("openapi/components/requestBodies.yaml")
OPENAPI_ROOT = Path("openapi")

def bundle_request_bodies():
    print("📦 Bundling requestBodies into components/requestBodies.yaml...")
    bundled = {"components": {"requestBodies": {}}}

    for file in REQUEST_BODIES_DIR.glob("*.yaml"):
        name = file.stem
        with file.open("r", encoding="utf-8") as f:
            content = yaml.safe_load(f) or {}

        if list(content.keys()) == [name]:
            body_def = content[name]
        elif len(content) == 1:
            actual_name, body_def = next(iter(content.items()))
            print(f"⚠️ Renaming top-level key from '{actual_name}' to '{name}' in {file.name}")
        else:
            print(f"❌ Skipping {file.name}: Invalid structure (must have exactly one top-level key)")
            continue

        bundled["components"]["requestBodies"][name] = body_def
        print(f"✅ Added: {name}")

    with REQUEST_BODIES_BUNDLE.open("w", encoding="utf-8") as f:
        yaml.safe_dump(bundled, f, sort_keys=False)

def rewrite_refs():
    print("🔁 Rewriting $ref: ./components/requestBodies/X.yaml → #/components/requestBodies/X")
    ref_pattern = re.compile(r"\.\/components\/requestBodies\/([\w\-]+)\.yaml")

    def normalize_refs(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == "$ref" and isinstance(v, str):
                    match = ref_pattern.match(v)
                    if match:
                        body_name = match.group(1)
                        obj[k] = f"#/components/requestBodies/{body_name}"
                else:
                    normalize_refs(v)
        elif isinstance(obj, list):
            for item in obj:
                normalize_refs(item)

    for root, _, files in os.walk(OPENAPI_ROOT):
        for fname in files:
            if fname.endswith((".yaml", ".yml")):
                path = Path(root) / fname
                try:
                    with path.open("r", encoding="utf-8") as f:
                        content = yaml.safe_load(f)
                except Exception as e:
                    print(f"❌ Skipping {path}: {e}")
                    continue

                if not content:
                    continue

                original = yaml.dump(content)
                normalize_refs(content)
                modified = yaml.dump(content)

                if original != modified:
                    with path.open("w", encoding="utf-8") as f:
                        yaml.safe_dump(content, f, sort_keys=False)
                    print(f"✏️ Rewritten refs in: {path}")

if __name__ == "__main__":
    bundle_request_bodies()
    rewrite_refs()
    print("\n🎉 Done! Request bodies bundled and refs rewritten.")
