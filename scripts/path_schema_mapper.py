import argparse
import json
from pathlib import Path

import yaml


def get_all_schemas(schemas_dir: Path) -> set:
    return {f.stem for f in schemas_dir.glob('*.yaml')}

def load_external_map(map_path: Path) -> dict:
    if map_path.suffix == '.json':
        with map_path.open() as f:
            return json.load(f)
    elif map_path.suffix in ('.yaml', '.yml'):
        with map_path.open() as f:
            return yaml.safe_load(f)
    else:
        raise ValueError("Unsupported map file format (use .json or .yaml)")

from pathlib import Path


def map_paths_to_schemas(schemas_dir, paths_dir, map_file):
    schema_names = get_all_schemas(schemas_dir)
    path_mappings = {}

    map_path = Path(map_file)
    if map_path.exists():
        external_map = load_external_map(map_file)
        for path_name, schema in external_map.items():
            if schema in schema_names:
                path_mappings[path_name] = schema
            else:
                print(f"⚠️ Warning: Schema '{schema}' not found in {schemas_dir}")
    else:
        print("⚠️ No external map provided → auto-generating map")
        for filename in os.listdir(paths_dir):
            if filename.endswith('.yaml'):
                path_name = filename.replace('.json.yaml', '').replace('.yaml', '')
                for schema in schema_names:
                    if schema.lower() in path_name.lower():
                        path_mappings[path_name] = schema
                        break

    return path_mappings


def save_yaml(data: dict, output_file: Path):
    with output_file.open('w') as f:
        yaml.safe_dump(data, f, sort_keys=False)

def main():
    parser = argparse.ArgumentParser(description="Map OpenAPI paths to schemas based on names or external map")
    parser.add_argument('--input', type=Path, required=True, help="Input split directory")
    parser.add_argument('--output', type=Path, required=True, help="Output YAML mapping file")
    parser.add_argument('--map', type=Path, help="Optional external map file (JSON or YAML)")
    args = parser.parse_args()

    schemas_dir = args.input / 'components' / 'schemas'
    paths_dir = args.input / 'paths'

    path_schema_map = map_paths_to_schemas(schemas_dir, paths_dir, args.map)
    save_yaml(path_schema_map, args.output)

    print(f"✅ Saved path-schema mapping → {args.output}")

if __name__ == "__main__":
    main()
