import sys, os, yaml
from pathlib import Path

input_dir = Path(sys.argv[1])
output_file = Path(sys.argv[2])

schemas_dir = input_dir / "components" / "schemas"
paths_dir = input_dir / "paths"

def get_all_schemas(schema_path):
    return [f.stem for f in schema_path.glob('*.yaml')]

def generate_map():
    schema_names = get_all_schemas(schemas_dir)
    path_mappings = {}

    for file in paths_dir.glob('*.yaml'):
        path_name = file.stem.replace('.json', '')
        for schema in schema_names:
            if schema.lower() in path_name.lower():
                path_mappings[path_name] = schema
                break

    return path_mappings

with output_file.open('w') as f:
    yaml.dump(generate_map(), f, sort_keys=False)

print(f"✅ Saved path-schema map → {output_file}")
