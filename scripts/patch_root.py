import argparse
from pathlib import Path

import yaml


def load_yaml_or_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        if path.suffix == ".json":
            import json
            return json.load(f)
        return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser(description="Patch root OpenAPI YAML with components from full spec")
    parser.add_argument("--input", type=Path, required=True, help="Modular root.yaml")
    parser.add_argument("--original", type=Path, required=True, help="Original full OpenAPI spec (yaml/json)")
    parser.add_argument("--output", type=Path, required=True, help="Patched root file to output")
    args = parser.parse_args()

    root = load_yaml_or_json(args.input)
    full = load_yaml_or_json(args.original)

    root["components"] = full.get("components", {})

    with args.output.open("w", encoding="utf-8") as f:
        yaml.safe_dump(root, f, sort_keys=False)

    print(f"✅ Patched {args.input} → {args.output} with components from {args.original}")

if __name__ == "__main__":
    main()
