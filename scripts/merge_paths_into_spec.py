import argparse
from pathlib import Path

import yaml


def get_all_schemas(schemas_dir: Path) -> set:
    return {f.stem for f in schemas_dir.glob('*.yaml')}

def load_external_map(map_path: Path) -> dict:
    if map_path.suffix in ['.yaml', '.yml']:
        with map_path.open(encoding='utf-8') as f:
            return yaml.safe_load(f)
    raise ValueError("Unsupported map file format (use .yaml or .yml)")

def map_paths_to_schemas(schemas_dir: Path, paths_dir: Path, map_file: Path = None) -> dict:
    schema_names = get_all_schemas(schemas_dir)
    path_mappings = {}

    if map_file and map_file.exists():
        external_map = load_external_map(map_file)
        for path_name, schema in external_map.items():
            if schema in schema_names:
                path_mappings[path_name] = schema
            else:
                print(f"⚠️ Warning: Schema '{schema}' not found in {schemas_dir}")
    else:
        print("⚠️ No external map provided → auto-generating map")
        for path_file in paths_dir.glob("*.yaml"):
            path_name = path_file.stem
            for schema in schema_names:
                if schema.lower() in path_name.lower():
                    path_mappings[path_name] = schema
                    break

    return path_mappings

def load_paths(paths_dir: Path) -> dict:
    merged_paths = {}
    for path_file in paths_dir.glob("*.yaml"):
        with path_file.open(encoding='utf-8') as f:
            content = yaml.safe_load(f)
            if not isinstance(content, dict):
                print(f"⚠️ Skipping invalid path file: {path_file}")
                continue
            for path_key, path_item in content.items():
                if not path_key.startswith('/'):
                    print(f"❌ Invalid path key in {path_file}: '{path_key}' must start with '/'")
                    continue
                if path_key in merged_paths:
                    merged_paths[path_key].update(path_item)
                else:
                    merged_paths[path_key] = path_item
    return merged_paths

def inject_paths_to_spec(spec_path: Path, output_path: Path, paths_dict: dict):
    with spec_path.open(encoding='utf-8') as f:
        spec = yaml.safe_load(f)

    spec.setdefault('paths', {})
    spec['paths'].update(paths_dict)

    with output_path.open('w', encoding='utf-8') as f:
        yaml.safe_dump(spec, f, sort_keys=False, allow_unicode=True)

    print(f"✅ Injected {len(paths_dict)} paths into → {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Map paths to schemas and inject into OpenAPI spec.")
    parser.add_argument('--input', type=Path, required=True, help="Directory containing OpenAPI components/paths.")
    parser.add_argument('--spec', type=Path, required=True, help="Path to OpenAPI root file.")
    parser.add_argument('--output', type=Path, required=True, help="Output file with merged paths.")
    parser.add_argument('--map', type=Path, help="Optional map file for path-to-schema mapping.")

    args = parser.parse_args()

    schemas_dir = args.input / 'components' / 'schemas'
    paths_dir = args.input / 'paths'

    map_paths_to_schemas(schemas_dir, paths_dir, args.map)  # still runs for diagnostics
    merged_paths = load_paths(paths_dir)
    inject_paths_to_spec(args.spec, args.output, merged_paths)

if __name__ == "__main__":
    main()
