from pathlib import Path

import yaml

SCHEMAS_DIR = Path("openapi/components/schemas")
OUTPUT_FILE = Path("openapi/components/schemas.yaml")

def bundle_schemas():
    bundled = {"components": {"schemas": {}}}

    for schema_file in SCHEMAS_DIR.glob("*.yaml"):
        schema_name = schema_file.stem
        with schema_file.open("r", encoding="utf-8") as f:
            try:
                schema_content = yaml.safe_load(f)
                if schema_content:
                    bundled["components"]["schemas"][schema_name] = schema_content
                    print(f"✅ Added: {schema_name}")
            except yaml.YAMLError as e:
                print(f"❌ Skipping {schema_file.name}: {e}")

    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        yaml.safe_dump(bundled, f, sort_keys=False)

    print(f"\n🎉 Bundled {len(bundled['components']['schemas'])} schemas → {OUTPUT_FILE}")

if __name__ == "__main__":
    bundle_schemas()
