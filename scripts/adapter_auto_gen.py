import os
from difflib import get_close_matches

# Paths
custom_model_dir = "clio_sdk/models"
sdk_model_dir = "clio_client/models"
adapter_dir = "clio_sdk/adapters"
os.makedirs(adapter_dir, exist_ok=True)

# List of your custom model files (e.g., matterbase.py)
custom_models = [
    f for f in os.listdir(custom_model_dir)
    if f.endswith(".py") and f != "__init__.py"
]
custom_bases = [f.replace(".py", "") for f in custom_models]

# List of SDK model base names (without .py)
sdk_models = [
    f.replace(".py", "") for f in os.listdir(sdk_model_dir)
    if f.endswith(".py")
]

# Generate adapter files with close match
adapter_scripts = {}
for base in custom_bases:
    match = get_close_matches(base.replace("base", ""), sdk_models, n=1)
    if match:
        sdk_class = match[0]
        class_base = base.capitalize()
        adapter_content = f"""# Adapter for {base}
from clio_sdk.models.{base} import {class_base}In, {class_base}Out, {class_base}Update, {class_base}Db
from clio_client.models import {sdk_class}

def convert_sdk_to_{base}out(src: {sdk_class}) -> {class_base}Out:
    return {class_base}Out(**src.dict())

def convert_{base}in_to_sdk(src: {class_base}In) -> {sdk_class}:
    return {sdk_class}(**src.dict())
"""
        adapter_scripts[base] = adapter_content
        with open(os.path.join(adapter_dir, f"adapter_{base}.py"), "w") as f:
            f.write(adapter_content)

adapter_scripts.keys()
