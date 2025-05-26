import yaml
from typing import Dict, Any

# Refactor of the JSON version to handle YAML
yaml_input_path = "final.normalized.yaml"
yaml_output_path = "openapi/openapi_corrected_types.yaml"

# Load YAML
with open(yaml_input_path, "r") as f:
    openapi_yaml_data = yaml.safe_load(f)

# Reuse the same correction logic for YAML
def correct_schema_types_yaml(openapi: Dict[str, Any]) -> Dict[str, Any]:
    parameters = openapi.get("components", {}).get("parameters", {})
    schemas = openapi.get("components", {}).get("schemas", {})

    param_types = {
        name: param.get("schema", {})
        for name, param in parameters.items()
        if "schema" in param
    }

    def update_fields(schema: Dict[str, Any]):
        if "properties" in schema:
            for prop_name, prop in schema["properties"].items():
                if prop_name in param_types:
                    param_def = param_types[prop_name]
                    prop.update({
                        k: v for k, v in param_def.items()
                        if k in {"type", "format", "enum", "minimum", "maximum", "pattern"}
                    })
        return schema

    updated_schemas = {
        name: update_fields(schema)
        for name, schema in schemas.items()
    }

    openapi["components"]["schemas"] = updated_schemas
    return openapi

# Apply corrections
corrected_openapi_yaml = correct_schema_types_yaml(openapi_yaml_data)

# Save corrected YAML
with open(yaml_output_path, "w") as f:
    yaml.dump(corrected_openapi_yaml, f, sort_keys=False)

yaml_output_path
