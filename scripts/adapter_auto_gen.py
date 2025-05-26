import os
from difflib import get_close_matches

def to_title_case(s):
    return "".join([part.capitalize() for part in s.replace("_", " ").split()])

custom_model_dir = "/home/solutionpartner/auditor/clio_sdk/models"
sdk_model_dir = "/home/solutionpartner/auditor/clio_client/models"
adapter_dir = "/home/solutionpartner/auditor/clio_sdk/adapters"
os.makedirs(adapter_dir, exist_ok=True)

custom_models = [
    f for f in os.listdir(custom_model_dir)
    if f.endswith(".py") and f != "__init__.py"
]
custom_bases = [f.replace(".py", "") for f in custom_models]

sdk_models = [
    f.replace(".py", "") for f in os.listdir(sdk_model_dir)
    if f.endswith(".py")
]

for base in custom_bases:
    match = get_close_matches(base.replace("base", ""), sdk_models, n=1)
    if match:
        sdk_class = match[0]
        class_base = to_title_case(base)
        sdk_class_title = to_title_case(sdk_class)
        import_classes = ", ".join([
            f"{class_base}In",
            f"{class_base}Out",
            f"{class_base}Update",
            f"{class_base}Db"
        ])
        adapter_content = f"""# Adapter for {base}
from clio_sdk.models.{base} import {import_classes}
from clio_client.models.{sdk_class} import {sdk_class_title}

def convert_sdk_to_{base}out(src: {sdk_class_title}) -> {class_base}Out:
    \"\"\"Converts a clio_client model to clio_sdk model.\"\"\"
    return {class_base}Out(**src.model_dump())

def convert_{base}in_to_sdk(src: {class_base}In) -> {sdk_class_title}:
    \"\"\"Converts a clio_sdk model to clio_client model.\"\"\"
    return {sdk_class_title}(**src.model_dump())
"""
        with open(os.path.join(adapter_dir, f"adapter_{base}.py"), "w") as f:
            f.write(adapter_content)
