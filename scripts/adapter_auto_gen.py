import os
import re
from difflib import get_close_matches


def to_pascal_case(s: str) -> str:
    # Converts snake_case or kebab-case or all-lowercase to PascalCase
    return ''.join(word.capitalize() for word in re.split(r'[_\-]', s.strip()) if word)

custom_model_dir = "clio_sdk/models"
sdk_model_dir = "clio_client/models"
adapter_dir = "clio_sdk/adapters"
os.makedirs(adapter_dir, exist_ok=True)

custom_bases = [
    f.replace(".py", "") for f in os.listdir(custom_model_dir)
    if f.endswith(".py") and f != "__init__.py"
]
sdk_bases = [
    f.replace(".py", "") for f in os.listdir(sdk_model_dir)
    if f.endswith(".py")
]

for base in custom_bases:
    # Try to match the base with the sdk_bases (strip 'base' if present)
    logical_base = base[:-5] if base.endswith("_base") else base
    match = get_close_matches(logical_base, sdk_bases, n=1)
    if match:
        sdk_file = match[0]
        # Use underscores for file names, PascalCase for class names
        class_prefix = to_pascal_case(base)
        sdk_class = to_pascal_case(sdk_file)
        adapter_code = f"""# Adapter for {class_prefix}
from clio_sdk.models.{base} import {class_prefix}In, {class_prefix}Out, {class_prefix}Update, {class_prefix}Db
from clio_client.models.{sdk_file} import {sdk_class}

def convert_sdk_to_{base}out(src: {sdk_class}) -> {class_prefix}Out:
    \"\"\"Converts a clio_client model to clio_sdk model.\"\"\"
    return {class_prefix}Out(**src.model_dump())

def convert_{base}in_to_sdk(src: {class_prefix}In) -> {sdk_class}:
    \"\"\"Converts a clio_sdk model to clio_client model.\"\"\"
    return {sdk_class}(**src.model_dump())
"""
        adapter_path = os.path.join(adapter_dir, f"adapter_{base}.py")
        with open(adapter_path, "w") as f:
            f.write(adapter_code)
        print(f"✅ Adapter written: {adapter_path}")