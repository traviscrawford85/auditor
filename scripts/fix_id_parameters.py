import argparse
import re
from pathlib import Path

import yaml


def fix_id_parameters(spec: dict) -> dict:
    """Ensure {id} path parameters are defined in operations."""
    for path, operations in spec.get('paths', {}).items():
        if '{id}' in path:
            for method, operation in operations.items():
                if isinstance(operation, dict):
                    parameters = operation.setdefault('parameters', [])
                    if not any(isinstance(p, dict) and p.get('name') == 'id' for p in parameters):
                        parameters.append({
                            'name': 'id',
                            'in': 'path',
                            'required': True,
                            'schema': {'type': 'string'}
                        })
    return spec

def rename_component_file(file_path: Path):
    # Example: activity_id|query.yaml → activity_id.yaml
    if '|query.yaml' in file_path.name or '|header.yaml' in file_path.name or '|path.yaml' in file_path.name:
        clean_name = re.sub(r'\|.*\.yaml$', '.yaml', file_path.name)
        new_path = file_path.parent / clean_name
        if new_path != file_path:
            file_path.rename(new_path)
            print(f"✅ Renamed parameter file → {new_path}")

def process_file(file_path: Path):
    with file_path.open() as f:
        spec = yaml.safe_load(f)

    updated_spec = fix_id_parameters(spec)

    with file_path.open('w') as f:
        yaml.safe_dump(updated_spec, f, sort_keys=False)

    print(f"✅ Fixed id parameters → {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Inject {id} path parameters and rename parameter files")
    parser.add_argument('--input-dir', type=Path, required=True, help="Input directory with YAML files")
    args = parser.parse_args()

    input_dir = args.input_dir.resolve()
    yaml_files = list(input_dir.glob('**/*.yaml'))

    if not yaml_files:
        print(f"⚠️ No YAML files found in {input_dir}")
        return

    for yaml_file in yaml_files:
        relative_path = yaml_file.relative_to(input_dir)

        # Match components/parameters files needing renaming
        if relative_path.match('components/parameters/*|*.yaml'):
            rename_component_file(yaml_file)

        # Match paths files (including subdirectories)
        elif relative_path.match('paths/**/*.yaml') or relative_path.match('paths/*.yaml') or yaml_file.name == 'root.yaml':
            process_file(yaml_file)


if __name__ == "__main__":
    main()
