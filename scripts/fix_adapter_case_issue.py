import os
import re

ADAPTER_DIR = "clio_sdk/adapters"

# Regular expressions to match incorrectly cased class names
camel_case_re = re.compile(r"\b([A-Z][a-z0-9]+)+\b")
incorrect_class_re = re.compile(r"\b([A-Z][a-z]+)(base|list|show|in|out|update|db)\b", re.IGNORECASE)

def to_pascal_case(name: str) -> str:
    parts = re.split(r'[_\s]', name)
    return ''.join(p.capitalize() for p in parts if p)

def fix_casing_in_file(filepath: str):
    with open(filepath, "r") as f:
        content = f.read()

    matches = incorrect_class_re.findall(content)
    for full_match, suffix in matches:
        old_name = full_match + suffix
        new_name = to_pascal_case(full_match + "_" + suffix)
        content = re.sub(rf"\b{old_name}\b", new_name, content)

    with open(filepath, "w") as f:
        f.write(content)
    return filepath

# Apply fix across adapter directory
fixed_files = []
for root, _, files in os.walk(ADAPTER_DIR):
    for filename in files:
        if filename.endswith(".py") and filename.startswith("adapter_"):
            full_path = os.path.join(root, filename)
            fixed_files.append(fix_casing_in_file(full_path))

fixed_files
