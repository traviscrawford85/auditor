import importlib
import inspect
import sys
from pathlib import Path
from typing import Dict, Type, get_args, get_origin

from pydantic import BaseModel

# Ensure root directory is in sys.path
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

# Directories
sdk_models_dir = ROOT_DIR / "clio_sdk" / "models"
client_models_dir = ROOT_DIR / "clio_client" / "models"
adapter_output_dir = ROOT_DIR / "clio_sdk" / "adapters_auto"
adapter_output_dir.mkdir(parents=True, exist_ok=True)

def pascal_case(s: str) -> str:
    return "".join(word.capitalize() for word in s.replace("_", " ").split())

def import_models(package: str, directory: Path) -> Dict[str, Type[BaseModel]]:
    models = {}
    for file in directory.glob("*.py"):
        if file.name == "__init__.py":
            continue
        module_name = f"{package}.{file.stem}"
        try:
            module = importlib.import_module(module_name)
        except Exception as e:
            print(f"❌ Failed to import {module_name}: {e}")
            continue
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, BaseModel) and obj.__module__ == module.__name__:
                models[name] = obj
    return models

sdk_models = import_models("clio_sdk.models", sdk_models_dir)
client_models = import_models("clio_client.models", client_models_dir)

def generate_field_conversion(field, src_type, dst_type, direction="sdk_to_custom"):
    if get_origin(dst_type) == list and get_origin(src_type) == list:
        dst_inner, src_inner = get_args(dst_type)[0], get_args(src_type)[0]
        if isinstance(dst_inner, type) and isinstance(src_inner, type) and \
           dst_inner.__name__ in sdk_models and src_inner.__name__ in client_models:
            call = f"convert_sdk_to_{dst_inner.__name__.lower()}" if direction == "sdk_to_custom" else f"convert_{dst_inner.__name__.lower()}_to_sdk"
            return f"[{call}(item) for item in src.{field}]"
    elif isinstance(dst_type, type) and isinstance(src_type, type):
        if dst_type.__name__ in sdk_models and src_type.__name__ in client_models:
            call = f"convert_sdk_to_{dst_type.__name__.lower()}" if direction == "sdk_to_custom" else f"convert_{dst_type.__name__.lower()}_to_sdk"
            return f"{call}(src.{field})"
    return f"src.{field}"

def generate_adapter_file(dst_model: Type[BaseModel], src_model: Type[BaseModel]):
    dst_name = dst_model.__name__
    src_name = src_model.__name__

    dst_file = dst_name.replace("Show", "").replace("List", "").replace("Out", "").replace("In", "").replace("Update", "").replace("Db", "").lower()
    src_file = src_name.replace("Show", "").replace("List", "").replace("Out", "").replace("In", "").replace("Update", "").replace("Db", "").lower()

    lines = [
        f"# Auto-generated adapter for {dst_name} <-> {src_name}",
        f"from clio_sdk.models.{dst_file} import {dst_name}",
        f"from clio_client.models.{src_file} import {src_name}",
        "",
        f"def convert_sdk_to_{dst_file}(src: {src_name}) -> {dst_name}:",
        f'    """Convert clio_client {src_name} to clio_sdk {dst_name}."""',
        f"    return {dst_name}(",
    ]
    for field, dst_field in dst_model.model_fields.items():
        if field in src_model.model_fields:
            src_type = src_model.model_fields[field].annotation
            dst_type = dst_field.annotation
            lines.append(f"        {field}={generate_field_conversion(field, src_type, dst_type)},")
    lines.append("    )\n")

    lines.append(f"def convert_{dst_file}_to_sdk(src: {dst_name}) -> {src_name}:")
    lines.append(f'    """Convert clio_sdk {dst_name} to clio_client {src_name}."""')
    lines.append(f"    return {src_name}(")
    for field, src_field in src_model.model_fields.items():
        if field in dst_model.model_fields:
            dst_type = dst_model.model_fields[field].annotation
            src_type = src_field.annotation
            lines.append(f"        {field}={generate_field_conversion(field, dst_type, src_type, direction='custom_to_sdk')},")
    lines.append("    )")

    with open(adapter_output_dir / f"adapter_{dst_file}.py", "w") as f:
        f.write("\n".join(lines))

# Match and generate adapters
for sdk_name, sdk_model in sdk_models.items():
    base_name = sdk_name.replace("Out", "").replace("In", "").replace("Update", "").replace("Db", "")
    for client_name, client_model in client_models.items():
        if client_name.lower().startswith(base_name.lower()):
            generate_adapter_file(sdk_model, client_model)
            break
