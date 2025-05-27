from pathlib import Path

import yaml


def patch_missing_types(directory: Path, output_log: Path):
    patched_files = []
    for file in directory.glob("*.yaml"):
        with file.open("r", encoding="utf-8") as f:
            content = yaml.safe_load(f) or {}

        if not content:
            continue

        modified = False
        for schema_name, schema_def in content.get("components", {}).get("schemas", {}).items():
            if "type" not in schema_def and "properties" in schema_def:
                schema_def["type"] = "object"
                modified = True
                patched_files.append(f"{file.name}: added type: object to schema '{schema_name}'")

        if modified:
            with file.open("w", encoding="utf-8") as f:
                yaml.safe_dump(content, f, sort_keys=False)

    with output_log.open("w", encoding="utf-8") as log:
        log.write("\n".join(patched_files))

    return patched_files

# Define the path to openapi components/schemas directory
schemas_path = Path("openapi/components/schemas")
log_path = Path("patched_schemas.log")

patched_log = patch_missing_types(schemas_path, log_path)
patched_log[:10]  # Preview first few patched entries
