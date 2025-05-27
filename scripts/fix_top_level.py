import argparse
from pathlib import Path

import yaml

try:
    from openapi_spec_validator import validate_spec
    VALIDATOR_AVAILABLE = True
except ImportError:
    VALIDATOR_AVAILABLE = False

def load_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)

def ensure_top_level(spec: dict, version: str = "3.0.0"):
    spec.setdefault("openapi", version)
    spec.setdefault("info", {
        "title": "Clio API Documentation",
        "version": "v4",
        "contact": {
            "name": "Clio API Support",
            "email": "api@clio.com"
        }
    })
    spec.setdefault("servers", [
        {"url": "https://app.clio.com/api/v4", "description": "US region Production Server"},
        {"url": "https://eu.app.clio.com/api/v4", "description": "Europe region Production Server"},
        {"url": "https://ca.app.clio.com/api/v4", "description": "Canada region Production Server"},
        {"url": "https://au.app.clio.com/api/v4", "description": "Australia region Production Server"}
    ])
    spec.setdefault("tags", [])
    spec.setdefault("paths", {})
    spec.setdefault("components", {})

def merge_openapi(root_file: Path, components_dir: Path, paths_dir: Path, output_file: Path, openapi_version: str):
    spec = load_yaml(root_file)
    ensure_top_level(spec, version=openapi_version)

    # Merge components
    if components_dir.exists():
        for comp_type_dir in components_dir.iterdir():
            if comp_type_dir.is_dir():
                comp_type = comp_type_dir.name
                spec["components"].setdefault(comp_type, {})
                for file in comp_type_dir.glob("*.yaml"):
                    name = file.stem
                    spec["components"][comp_type][name] = load_yaml(file)

    # Merge paths with multi-path support
    operation_ids = set()
    if paths_dir.exists():
        for file in paths_dir.glob("*.yaml"):
            file_data = load_yaml(file)
            if not isinstance(file_data, dict):
                continue
            for path_key, methods in file_data.items():
                if path_key not in spec["paths"]:
                    spec["paths"][path_key] = methods
                else:
                    spec["paths"][path_key].update(methods)

                # Collect operationId for validation
                for method_def in methods.values():
                    op_id = method_def.get("operationId")
                    if op_id:
                        if op_id in operation_ids:
                            raise ValueError(f"Duplicate operationId found: {op_id} in file {file}")
                        operation_ids.add(op_id)

    # Output the merged file
    with output_file.open("w", encoding="utf-8") as f:
        yaml.safe_dump(spec, f, sort_keys=False, allow_unicode=True)

    print(f"✅ Fully merged spec → {output_file}")

    # Optional: validate spec
    if VALIDATOR_AVAILABLE:
        try:
            validate_spec(spec)
            print("✅ OpenAPI spec is valid.")
        except Exception as e:
            print(f"⚠️ Validation failed: {e}")
    else:
        print("ℹ️ Validation skipped (install openapi-spec-validator for automatic validation).")

def main():
    parser = argparse.ArgumentParser(description="Merge modular OpenAPI segments into one document")
    parser.add_argument("--root", type=Path, required=True, help="Root OpenAPI YAML file")
    parser.add_argument("--components", type=Path, help="Components directory")
    parser.add_argument("--paths", type=Path, help="Paths directory")
    parser.add_argument("--output", type=Path, required=True, help="Output merged YAML file")
    parser.add_argument("--version", type=str, default="3.0.0", help="OpenAPI version (default: 3.0.0)")
    args = parser.parse_args()

    merge_openapi(args.root, args.components or Path(), args.paths or Path(), args.output, args.version)

if __name__ == "__main__":
    main()
