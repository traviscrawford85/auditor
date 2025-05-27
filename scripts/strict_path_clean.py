# Rebuild the OpenAPI full spec from modular components and paths, using cleaned and verified structure
from pathlib import Path

import yaml

BASE_DIR = Path("openapi")
ROOT_FILE = BASE_DIR / "root.yaml"
COMPONENTS_DIR = BASE_DIR / "components"
PATHS_DIR = BASE_DIR / "paths"
OUTPUT_FILE = BASE_DIR / "bundled/final.cleaned.yaml"
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

def load_yaml(file: Path) -> dict:
    if not file.exists():
        return {}
    with file.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def merge_openapi_spec(root_file, components_dir, paths_dir, output_file):
    spec = load_yaml(root_file)
    spec.setdefault("openapi", "3.0.0")
    spec.setdefault("info", {"title": "Merged Spec", "version": "1.0"})
    spec.setdefault("paths", {})
    spec.setdefault("components", {})

    for comp_type_dir in components_dir.iterdir():
        if comp_type_dir.is_dir():
            comp_type = comp_type_dir.name
            spec["components"].setdefault(comp_type, {})
            for comp_file in comp_type_dir.glob("*.yaml"):
                comp_name = comp_file.stem
                spec["components"][comp_type][comp_name] = load_yaml(comp_file)

    for path_file in paths_dir.glob("*.yaml"):
        path_key = "/" + path_file.stem.replace("__", "/").replace("_.", ".").replace("_", "/")
        path_data = load_yaml(path_file)
        if isinstance(path_data, dict) and path_key not in spec["paths"]:
            spec["paths"][path_key] = path_data

    with output_file.open("w", encoding="utf-8") as f:
        yaml.safe_dump(spec, f, sort_keys=False)
    print(f"✅ Rebuilt full spec → {output_file}")

merge_openapi_spec(ROOT_FILE, COMPONENTS_DIR, PATHS_DIR, OUTPUT_FILE)
