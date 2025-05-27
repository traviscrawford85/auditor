import json
from pathlib import Path

import yaml

PARAMS_FILE = Path("openapi/components/parameters.yaml")
SCHEMAS_DIR = Path("openapi/components/schemas")
OUTPUT_FILE = Path("openapi/components/parameter_schema_mapping.json")

def load_parameters():
    with PARAMS_FILE.open("r", encoding="utf-8") as f:
        params = yaml.safe_load(f)["components"]["parameters"]
    return params

def load_schema_names():
    return {f.stem.lower(): f.name for f in SCHEMAS_DIR.glob("*.yaml")}

def derive_mapping():
    params = load_parameters()
    schema_names = load_schema_names()
    mapping = {}
    for pname, pdef in params.items():
        base = pname.lower().replace("_id", "").replace("[]", "")
        # Try direct match
        if base in schema_names:
            mapping[pname] = schema_names[base]
        else:
            # Try singular/plural or other heuristics as needed
            for sname in schema_names:
                if base in sname or sname in base:
                    mapping[pname] = schema_names[sname]
                    break
    return mapping

if __name__ == "__main__":
    mapping = derive_mapping()
    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(mapping, f, indent=2)
    print(f"✅ Mapping written to {OUTPUT_FILE}")