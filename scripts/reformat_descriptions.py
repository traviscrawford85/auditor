import os
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import LiteralScalarString

OPENAPI_DIR = "./openapi"

yaml = YAML()
yaml.preserve_quotes = True
yaml.indent(mapping=2, sequence=4, offset=2)

def format_multiline(text):
    if isinstance(text, str) and ('\\n' in text or '\n' in text or len(text) > 100):
        return LiteralScalarString(text.replace('\\n', '\n').replace('\\"', '"'))
    return text

def transform_descriptions(node):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "description":
                node[k] = format_multiline(v)
            else:
                transform_descriptions(v)
    elif isinstance(node, list):
        for i in node:
            transform_descriptions(i)

def process_file(filepath):
    with open(filepath, "r") as f:
        data = yaml.load(f)

    if not data:
        return

    transform_descriptions(data)

    with open(filepath, "w") as f:
        yaml.dump(data, f)
        print(f"✅ Reformatted descriptions in: {filepath}")

def process_all_yaml():
    for subdir, _, files in os.walk(OPENAPI_DIR):
        for file in files:
            if file.endswith((".yaml", ".yml")):
                process_file(os.path.join(subdir, file))

if __name__ == "__main__":
    process_all_yaml()
