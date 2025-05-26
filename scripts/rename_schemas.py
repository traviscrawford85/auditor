from pathlib import Path
import yaml

SCHEMAS_DIR = Path("openapi/components/schemas")

def rename_individual_schema_files():
    for file in SCHEMAS_DIR.glob("*.yaml"):
        with file.open("r", encoding="utf-8") as f:
            content = yaml.safe_load(f)

        if not content or not isinstance(content, dict):
            continue

        # Expecting a single top-level key like "UnnamedSchema"
        old_key = list(content.keys())[0]
        schema = content[old_key]

        if old_key != "UnnamedSchema":
            continue

        # Derive new name from description
        description = schema.get("description", "Unnamed")
        new_key = description.strip().replace(" ", "").replace("-", "").replace(".", "")

        # Replace key and rewrite file
        content = {new_key: schema}
        new_filename = f"{new_key}.yaml"
        new_path = SCHEMAS_DIR / new_filename

        with new_path.open("w", encoding="utf-8") as f:
            yaml.safe_dump(content, f, sort_keys=False)
        print(f"✅ Renamed {file.name} → {new_filename}")

        file.unlink()  # Remove old file

if __name__ == "__main__":
    rename_individual_schema_files()
