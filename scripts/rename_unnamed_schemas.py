from pathlib import Path

import yaml

# Directory containing component schemas
SCHEMAS_DIR = Path("openapi/components/schemas")

# Script to rename 'UnnamedSchema' to its description and extract $defs if present
def rename_unnamed_and_extract_defs():
    for file in SCHEMAS_DIR.glob("*.yaml"):
        with file.open("r", encoding="utf-8") as f:
            content = yaml.safe_load(f)

        if not content or "components" not in content or "schemas" not in content["components"]:
            continue

        schemas = content["components"]["schemas"]
        updated_schemas = {}
        extracted_defs = {}

        for name, schema in schemas.items():
            if "UnnamedSchema" in schema:
                candidate = schema["UnnamedSchema"]
                new_name = candidate.get("description", "Unnamed").replace(" ", "")
                updated_schemas[new_name] = {k: v for k, v in candidate.items() if k != "$defs"}

                if "$defs" in candidate:
                    for def_name, def_schema in candidate["$defs"].items():
                        extracted_defs[def_name] = def_schema
            else:
                updated_schemas[name] = schema

        # Merge extracted defs if any
        for def_name, def_schema in extracted_defs.items():
            if def_name not in updated_schemas:
                updated_schemas[def_name] = def_schema
            else:
                # Avoid overwriting existing schema names
                new_def_name = f"{def_name}_from_def"
                updated_schemas[new_def_name] = def_schema

        content["components"]["schemas"] = updated_schemas

        with file.open("w", encoding="utf-8") as f:
            yaml.safe_dump(content, f, sort_keys=False)
        print(f"✅ Updated: {file.name}")

rename_unnamed_and_extract_defs()
