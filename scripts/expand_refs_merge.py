from pathlib import Path
from typing import Any, Dict

import yaml

# Define the base directory structure
input_file = Path("openapi/root.patched.yaml")
components_dir = Path("openapi/components")
output_file = Path("openapi/expanded_full.yaml")

# Load base OpenAPI spec
with input_file.open("r", encoding="utf-8") as f:
    spec = yaml.safe_load(f)

# Load all components into a cache
component_cache: Dict[str, Dict[str, Any]] = {}

def load_yaml(file_path: Path) -> dict:
    with file_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

# Merge all component sections
for file in components_dir.glob("*.yaml"):
    section_name = file.stem
    section_data = load_yaml(file)
    if section_name in spec.get("components", {}):
        spec["components"][section_name].update(section_data.get(section_name, section_data))
    else:
        if "components" not in spec:
            spec["components"] = {}
        spec["components"][section_name] = section_data.get(section_name, section_data)
    component_cache[section_name] = spec["components"][section_name]

# Flatten refs in paths
def resolve_ref(ref: str) -> Any:
    if not ref.startswith("#/components/"):
        return {"$ref": ref}
    _, _, path = ref.partition("#/components/")
    section, _, item = path.partition("/")
    return component_cache.get(section, {}).get(item, {"$ref": ref})

def deref_node(node: Any) -> Any:
    if isinstance(node, dict):
        if "$ref" in node:
            resolved = resolve_ref(node["$ref"])
            merged = {**resolved, **{k: v for k, v in node.items() if k != "$ref"}}
            return deref_node(merged)
        return {k: deref_node(v) for k, v in node.items()}
    elif isinstance(node, list):
        return [deref_node(i) for i in node]
    return node

# Apply dereferencing to all operations in paths
for path, methods in spec.get("paths", {}).items():
    for method, op in methods.items():
        if isinstance(op, dict):
            for field in ("parameters", "requestBody", "responses"):
                if field in op:
                    op[field] = deref_node(op[field])

# Save the fully expanded output
with output_file.open("w", encoding="utf-8") as f:
    yaml.safe_dump(spec, f, sort_keys=False)

output_file.name
