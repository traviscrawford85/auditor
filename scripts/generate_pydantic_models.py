import os

SCHEMA_DIR = "./openapi/components/schemas"
MODEL_DIR = "./pydantic_models"
MODEL_TEMPLATE = '''from pydantic import BaseModel
from typing import Optional, List


class {name}In(BaseModel):
    """Incoming model for creating a {name}"""
    # TODO: Add fields


class {name}Out(BaseModel):
    """Outgoing model for returning a {name}"""
    # TODO: Add fields


class {name}Update(BaseModel):
    """Update model for patching a {name}"""
    # TODO: Add fields


class {name}Db(BaseModel):
    """Internal DB representation for {name}"""
    # TODO: Add fields
'''

os.makedirs(MODEL_DIR, exist_ok=True)

generated = []

for file in os.listdir(SCHEMA_DIR):
    if file.endswith(".yaml"):
        schema_name = os.path.splitext(file)[0]
        if schema_name.lower().endswith("base") or schema_name == "UnnamedSchema":
            continue
        name = "".join(word.capitalize() for word in schema_name.split("_"))
        model_code = MODEL_TEMPLATE.format(name=name)
        output_path = os.path.join(MODEL_DIR, f"{name}.py")
        with open(output_path, "w") as f:
            f.write(model_code)
        generated.append(name)

print("✅ Generated Pydantic models for:")
for model in generated:
    print(f"  - {model}")
