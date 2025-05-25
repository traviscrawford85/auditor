import argparse
import yaml
from pathlib import Path

def fix_types(obj):
    if isinstance(obj, dict):
        if 'properties' in obj and 'type' not in obj:
            obj['type'] = 'object'
        for key, value in obj.items():
            if key == "properties" and isinstance(value, dict):
                for prop_key, prop_val in value.items():
                    if isinstance(prop_val, dict) and "type" not in prop_val and "$ref" not in prop_val:
                        prop_val["type"] = "string"
            fix_types(value)
    elif isinstance(obj, list):
        for item in obj:
            fix_types(item)


def process_file(input_file: Path, output_file: Path):
    with input_file.open() as f:
        spec = yaml.safe_load(f)
    fix_types(spec)
    with output_file.open('w') as f:
        yaml.safe_dump(spec, f, sort_keys=False)
    print(f"✅ Fixed types → {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Add missing schema types")
    parser.add_argument('--input-dir', type=Path, required=True, help="Input directory")
    parser.add_argument('--output-dir', type=Path, required=True, help="Output directory")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)

    for file in args.input_dir.glob('*.yaml'):
        process_file(file, args.output_dir / file.name)

if __name__ == "__main__":
    main()
