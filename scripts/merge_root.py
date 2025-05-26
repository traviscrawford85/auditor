import yaml
from pathlib import Path
import re

ROOT_PATH = Path("openapi/final_bundle.yaml")
PATHS_DIR = Path("openapi/paths")
OUT_PATH = Path("openapi/final.merged.yaml")

def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def normalize_refs(obj):
    """Fix $ref paths like './components/parameters/X.yaml' → 'components/parameters.yaml#/components/parameters/X'"""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "$ref" and isinstance(v, str) and "components/" in v:
                match = re.match(r"\.\/?components\/(\w+)\/([\w\-]+)\.yaml", v)
                if match:
                    section, name = match.groups()
                    obj[k] = f"components/{section}.yaml#/components/{section}/{name}"
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
        path_key = "/" + path_file.stem.replace("__", "/").replace("_.", ".").replace("_", "/")
        paths[path_key] = content.get(path_key) or content  # in case already wrapped
    return paths

def main():
    spec = load_yaml(ROOT_PATH)
    spec["paths"] = load_and_wrap_paths()

    with OUT_PATH.open("w", encoding="utf-8") as f:
        yaml.safe_dump(spec, f, sort_keys=False)
    print(f"✅ Merged full spec written to: {OUT_PATH}")

if __name__ == "__main__":
    main()
