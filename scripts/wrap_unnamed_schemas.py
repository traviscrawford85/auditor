import os
import yaml

OPENAPI_ROOT = "./openapi/components/schemas"
WRAP_LOG = "wrapped_schemas_log.txt"
RESERVED_KEYS = {
    "type", "properties", "required", "description", "title",
    "allOf", "anyOf", "oneOf", "not", "items", "enum", "format", "default", "nullable"
}

def wrap_unnamed_schemas():
    log = []
    for file in os.listdir(OPENAPI_ROOT):
        if file.endswith(".yaml"):
            path = os.path.join(OPENAPI_ROOT, file)
            with open(path, "r") as f:
                try:
                    content = yaml.safe_load(f)
                    if content and isinstance(content, dict):
                        keys = list(content.keys())
                        if all(k in RESERVED_KEYS for k in keys):
                            wrapped = {"UnnamedSchema": content}
                            with open(path, "w") as wf:
                                yaml.dump(wrapped, wf, sort_keys=False)
                            log.append(f"{file} wrapped as UnnamedSchema")
                            print(f"✅ Wrapped {file}")
                except yaml.YAMLError:
                    print(f"⚠️ Skipped {file} due to YAML error")
    with open(os.path.join(OPENAPI_ROOT, WRAP_LOG), "w") as log_file:
        for entry in log:
            log_file.write(entry + "\n")

wrap_unnamed_schemas()
