import yaml
from pathlib import Path
import re

ROOT_PATH = Path("openapi/final_bundle.yaml")
PATHS_DIR = Path("openapi/paths")
COMPONENTS_BUNDLE = Path("openapi/components.yaml")
OUT_PATH = Path("openapi/final.merged.yaml")

def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def normalize_refs(obj):
    """Fix $ref paths like './components/parameters/X.yaml' → '#/components/parameters/X'"""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "$ref" and isinstance(v, str):
                match = re.match(r"\.\/components\/(\w+)\/([\w\-]+)\.yaml", v)
                if match:
                    section, name = match.groups()
                    obj[k] = f"#/components/{section}/{name}"
            else:
                normalize_refs(v)
    elif isinstance(obj, list):
        for item in obj:
            normalize_refs(item)

def load_and_wrap_paths():
    paths = {}
    for path_file in PATHS_DIR.glob("*.yaml"):
        content = load_yaml(path_file)
        normalize_refs(content)
        if len(content) == 1 and next(iter(content)).startswith("/"):
            path_key = next(iter(content))
            paths[path_key] = content[path_key]
        else:
            path_key = "/" + path_file.stem.replace("__", "/").replace("_.", ".").replace("_", "/")
            paths[path_key] = content
    return paths

def main():
    root_spec = load_yaml(ROOT_PATH)
    components = load_yaml(COMPONENTS_BUNDLE).get("components", {})
    paths = load_and_wrap_paths()

    root_spec["paths"] = paths
    root_spec["components"] = components

    with OUT_PATH.open("w", encoding="utf-8") as f:
        yaml.safe_dump(root_spec, f, sort_keys=False)
    print(f"✅ Full OpenAPI spec merged and written to: {OUT_PATH}")

if __name__ == "__main__":
    main()
