import re
from pathlib import Path

import yaml

# Paths
INPUT_SPEC = Path("openapi/final.merged.yaml")
OUTPUT_SPEC = Path("openapi/final.normalized.yaml")

# Ref pattern for ./schemas/XYZ.yaml
SCHEMA_REF_PATTERN = re.compile(r"\.\/schemas\/([\w\-]+)\.yaml")

def normalize_refs_in_spec(data):
    def recurse(obj):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == "$ref" and isinstance(v, str):
                    match = SCHEMA_REF_PATTERN.match(v)
                    if match:
                        schema_name = match.group(1)
                        obj[k] = f"components/schemas.yaml#/components/schemas/{schema_name}"
                else:
                    recurse(v)
        elif isinstance(obj, list):
            for item in obj:
                recurse(item)
    recurse(data)

# Load original spec
with INPUT_SPEC.open("r", encoding="utf-8") as f:
    spec = yaml.safe_load(f)

# Normalize
normalize_refs_in_spec(spec)

# Write output
with OUTPUT_SPEC.open("w", encoding="utf-8") as f:
    yaml.safe_dump(spec, f, sort_keys=False)

OUTPUT_SPEC.name
