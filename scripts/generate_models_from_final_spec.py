import os
import yaml
from typing import Any, List

INPUT_FILE = "openapi_final_cleaned.yaml"
OUTPUT_DIR = "clio_sdk/models"
ADAPTER_DIR = "clio_sdk/adapters"
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(ADAPTER_DIR, exist_ok=True)

def pascal_case(name: str) -> str:
    return "".join(word.capitalize() for word in name.split("_"))

# Load spec and schemas globally
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    spec = yaml.safe_load(f)

schemas = spec.get("components", {}).get("schemas", {})

def resolve_ref_schema(ref: str) -> dict:
    """ Given a $ref string like #/components/schemas/User, return the actual schema. """
    ref_name = ref.split("/")[-1]
    return schemas.get(ref_name, {})

def infer_type(prop):
    if "$ref" in prop:
        ref_name = prop["$ref"].split("/")[-1]
        return pascal_case(ref_name)
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
    if "$ref" in schema:
        schema = resolve_ref_schema(schema["$ref"])
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
    path = os.path.join(OUTPUT_DIR, f"{base_name.lower()}.py")
    with open(path, "w") as f:
        f.write("from pydantic import BaseModel\n")
        f.write("from typing import Optional, Any, List\n")
        f.write("from datetime import datetime\n\n")
        for suffix in ["In", "Out", "Update", "Db"]:
            model = generate_model_class(base_name, fields, suffix)
            f.write(model + "\n\n")
    print(f"✅ Model file created: {path}")

def write_adapter(base_name):
    file_name = f"adapter_{base_name.lower()}.py"
    path = os.path.join(ADAPTER_DIR, file_name)
    with open(path, "w") as f:
        f.write(f"# Adapter stubs for {base_name}\n")
        f.write(
            f"from clio_sdk.models.{base_name.lower()} import "
            f"{base_name}In, {base_name}Out, {base_name}Update, {base_name}Db\n"
        )
        f.write(
            f"def convert_sdk_to_{base_name.lower()}out(sdk_obj):\n"
            f"    # TODO\n    return {base_name}Out()\n\n"
        )
        f.write(
            f"def convert_{base_name.lower()}in_to_sdk(model):\n"
            f"    # TODO\n    return None\n"
        )
    print(f"✅ Adapter stub created: {path}")

# Process schemas
for name, schema in schemas.items():
    if not isinstance(schema, dict) or ("properties" not in schema and "$ref" not in schema):
        continue
    fields = extract_fields(schema)
    base_name = pascal_case(name)
    write_models(base_name, fields)
    write_adapter(base_name)
