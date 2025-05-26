from pathlib import Path
import yaml

SCHEMAS_DIR = Path("openapi/components/schemas")

def patch_id_types():
    print("🔍 Scanning for incorrect 'id' property types...")
    updated_count = 0
    skipped = 0

    for file in SCHEMAS_DIR.glob("*.yaml"):
        try:
            with file.open("r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"❌ YAML error in {file.name}: {e}")
            skipped += 1
            continue

        if not data or not isinstance(data, dict):
            print(f"⚠️  Skipping {file.name}: not a dict or empty.")
            skipped += 1
            continue

        changed = False
        # Support both wrapped (SchemaName: {...}) and flat style
        schema_items = data.items() if len(data) > 0 else []
        for schema_key, schema_value in schema_items:
            if not isinstance(schema_value, dict):
                continue
            props = schema_value.get("properties", {})
            if not isinstance(props, dict):
                continue
            if "id" in props:
                id_prop = props["id"]
                # Check for bad type: string, and replace it
                if isinstance(id_prop, dict) and id_prop.get("type") == "string":
                    id_prop["type"] = "integer"
                    changed = True
                # Check for anyOf with string + null, change to integer + null
                if isinstance(id_prop, dict) and "anyOf" in id_prop:
                    for variant in id_prop["anyOf"]:
                        if variant.get("type") == "string":
                            variant["type"] = "integer"
                            changed = True

        if changed:
            updated_count += 1
            with file.open("w", encoding="utf-8") as f:
                yaml.safe_dump(data, f, sort_keys=False)
            print(f"✅ Updated 'id' type in {file.name}")

    print(f"\n🎉 Completed. Patched {updated_count} schema files. Skipped {skipped} files.")

if __name__ == "__main__":
    patch_id_types()
