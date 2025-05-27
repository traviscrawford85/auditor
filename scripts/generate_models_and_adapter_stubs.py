import os
import re
from typing import List, Set, Tuple

import yaml

# Constants
INPUT_FILE = "openapi_final_cleaned.yaml"
OUTPUT_DIR = "clio_sdk/models"
ADAPTER_DIR = "clio_sdk/adapters"
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(ADAPTER_DIR, exist_ok=True)

def pascal_case(name: str) -> str:
    return ''.join(word.capitalize() for word in re.split(r'[_\-]', name) if word)

def snake_case(name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

# Load OpenAPI spec
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    spec = yaml.safe_load(f)

schemas = spec.get("components", {}).get("schemas", {})

def resolve_ref_schema(ref: str) -> dict:
    ref_name = ref.split("/")[-1]
    return schemas.get(ref_name, {})

def infer_type(prop: dict, dependencies: Set[str], variant: str) -> str:
    if "$ref" in prop:
        ref_name = prop["$ref"].split("/")[-1]
        class_base = pascal_case(ref_name)
        class_name = f"{class_base}{variant}"
        dependencies.add(class_base)
        return class_name
    t = prop.get("type", "Any")
    if t == "array":
        return f"List[{infer_type(prop.get('items', {}), dependencies, variant)}]"
    return {
        "string": "str",
        "integer": "int",
        "number": "float",
        "boolean": "bool",
        "object": "dict"
    }.get(t, "Any")

def extract_fields(schema: dict, dependencies: Set[str], variant: str) -> List[Tuple[str, str, bool]]:
    if "$ref" in schema:
        schema = resolve_ref_schema(schema["$ref"])
    props = schema.get("properties", {})
    required = set(schema.get("required", []))
    return [(name, infer_type(defn, dependencies, variant), name in required) for name, defn in props.items()]

def generate_model_class(name: str, fields: List[Tuple[str, str, bool]], suffix: str) -> str:
    lines = [f"class {name}{suffix}(BaseModel):"]
    if not fields:
        lines.append("    pass")
    else:
        for fname, ftype, required in fields:
            line = f"    {fname}: {ftype}" if required else f"    {fname}: Optional[{ftype}] = None"
            lines.append(line)
    return "\n".join(lines)

def write_models(base_name: str, all_fields: dict):
    file_name = snake_case(base_name)
    path = os.path.join(OUTPUT_DIR, f"{file_name}.py")
    with open(path, "w") as f:
        f.write("from pydantic import BaseModel\n")
        f.write("from typing import Optional, Any, List\n")
        f.write("from datetime import datetime\n")

        # Collect all dependencies across variants
        all_deps = set(dep for _, deps in all_fields.values() for dep in deps)
        for dep in sorted(all_deps):
            if dep != base_name:
                dep_file = snake_case(dep)
                f.write(f"from .{dep_file} import {dep}Out\n")  # Import one consistent variant

        f.write("\n")
        for suffix in ["In", "Out", "Update", "Db"]:
            model = generate_model_class(base_name, all_fields[suffix][0], suffix)
            f.write(model + "\n\n")

def write_adapter(base_name: str):
    file_name = snake_case(base_name)
    path = os.path.join(ADAPTER_DIR, f"adapter_{file_name}.py")
    with open(path, "w") as f:
        f.write(f"# Adapter stubs for {base_name}\n")
        f.write(f"from clio_sdk.models.{file_name} import {base_name}In, {base_name}Out, {base_name}Update, {base_name}Db\n\n")
        f.write(f"def convert_sdk_to_{file_name}out(sdk_obj):\n    # TODO\n    return {base_name}Out()\n\n")
        f.write(f"def convert_{file_name}in_to_sdk(model):\n    # TODO\n    return None\n")

# Process schemas
for name, schema in schemas.items():
    if not isinstance(schema, dict) or ("properties" not in schema and "$ref" not in schema):
        continue

    base_name = pascal_case(name)
    all_fields = {}
    for variant in ["In", "Out", "Update", "Db"]:
        deps = set()
        fields = extract_fields(schema, deps, variant)
        all_fields[variant] = (fields, deps)

    write_models(base_name, all_fields)
    write_adapter(base_name)

print("✅ Models and adapters regenerated with dependency-aware imports and consistent type references.")
