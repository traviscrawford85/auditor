import os
import re
from pathlib import Path

import yaml

PARAMETERS_DIR = Path("openapi/components/parameters")
PARAMETERS_BUNDLE = Path("openapi/components/parameters.yaml")
OPENAPI_ROOT = Path("openapi")

def bundle_parameters():
    print("📦 Bundling parameters into components/parameters.yaml...")
    bundled = {"components": {"parameters": {}}}

    for file in PARAMETERS_DIR.glob("*.yaml"):
        name = file.stem
        with file.open("r", encoding="utf-8") as f:
            content = yaml.safe_load(f)
            if content:
                bundled["components"]["parameters"][name] = content
                print(f"✅ Added: {name}")

    with PARAMETERS_BUNDLE.open("w", encoding="utf-8") as f:
        yaml.safe_dump(bundled, f, sort_keys=False)

def rewrite_refs():
    print("🔁 Rewriting $ref: ./X.yaml → #/components/parameters/X")
    ref_pattern = re.compile(r"\.\/components\/parameters\/([\w\-]+)\.yaml")

    def normalize_refs(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == "$ref" and isinstance(v, str):
                    match = ref_pattern.match(v)
                    if match:
                        param_name = match.group(1)
                        obj[k] = f"#/components/parameters/{param_name}"
                else:
                    normalize_refs(v)
        elif isinstance(obj, list):
            for item in obj:
                normalize_refs(item)

    for root, _, files in os.walk(OPENAPI_ROOT):
        for fname in files:
            if fname.endswith(".yaml") or fname.endswith(".yml"):
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
    bundle_parameters()
    rewrite_refs()
    print("\n🎉 Done! Parameters bundled and refs rewritten.")
