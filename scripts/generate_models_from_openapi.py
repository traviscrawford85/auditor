# Updated model generator for expanded_full.yaml (inlined OpenAPI spec)
import os

import yaml

INPUT_FILE = "openapi/expanded_full.yaml"
OUTPUT_DIR = "./schemas/from_expanded"
ADAPTER_DIR = "./adapters/from_expanded"
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(ADAPTER_DIR, exist_ok=True)

def pascal_case(name: str) -> str:
    # Ensures TitleCase (PascalCase) for all model class names
    return "".join(word.capitalize() for word in name.replace("-", "_").split("_") if word)

def infer_type(prop):
    t = prop.get("type", "Any")
    if t == "string" and prop.get("format") == "date-time":
        return "datetime"
    if t == "integer":
        return "int"
    if t == "string":
        return "str"
    if t == "boolean":
        return "bool"
    if t == "number":
        return "float"
    if t == "array":
        return f"List[{infer_type(prop.get('items', {}))}]"
    return "Any"

def extract_fields(schema):
    props = schema.get("properties", {})
    required = set(schema.get("required", []))
    fields = []
    for name, definition in props.items():
        typ = infer_type(definition)
        is_required = name in required
        fields.append((name, typ, is_required))
    return fields

def generate_model_class(name, fields, suffix):
    lines = [f"class {name}{suffix}(BaseModel):"]
    if not fields:
        lines.append("    pass")
    else:
        for fname, ftype, required in fields:
            if required:
                lines.append(f"    {fname}: {ftype}")
            else:
                lines.append(f"    {fname}: Optional[{ftype}] = None")
    return "\n".join(lines)

def write_models(base_name, fields):
    # Use TitleCase for the filename as well
    file_name = f"{base_name}.py"
    path = os.path.join(OUTPUT_DIR, file_name)
    with open(path, "w") as f:
        f.write("from pydantic import BaseModel\n")
        f.write("from typing import Optional, Any, List\n")
        f.write("from datetime import datetime\n\n")
        for suffix in ["In", "Out", "Update", "Db"]:
            model = generate_model_class(base_name, fields, suffix)
            f.write(model + "\n\n")
    print(f"✅ Model file created: {path}")

def write_adapter(base_name):
    # Use TitleCase for the filename as well
    file_name = f"adapter_{base_name.lower()}.py"
    path = os.path.join(ADAPTER_DIR, file_name)
    with open(path, "w") as f:
        f.write(f"# Adapter stubs for {base_name}\n")
        f.write(f"from schemas.from_expanded.{base_name} import {base_name}In, {base_name}Out, {base_name}Update, {base_name}Db\n\n")
        f.write(f"def convert_sdk_to_{base_name.lower()}out(sdk_obj):\n    # TODO\n    return {base_name}Out()\n\n")
        f.write(f"def convert_{base_name.lower()}in_to_sdk(model):\n    # TODO\n    return None\n")
    print(f"✅ Adapter stub created: {path}")

# Load the inlined OpenAPI spec and iterate components.schemas
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    spec = yaml.safe_load(f)

schemas = spec.get("components", {}).get("schemas", {})
for name, schema in schemas.items():
    if not isinstance(schema, dict) or "properties" not in schema:
        continue
    base_name = pascal_case(name)
    fields = extract_fields(schema)
    write_models(base_name, fields)
    write_adapter(base_name)

