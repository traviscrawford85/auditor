import os
import yaml
import re
from pathlib import Path

MODULAR_ROOT = "./openapi"
REPEATED = re.compile(r"(components/)+")

def normalize_modular_ref(ref: str) -> str:
    if not isinstance(ref, str) or "components" not in ref:
        return ref

    # Remove OpenAPI-invalid suffixes like "|header"
    ref = re.sub(r"\|.*$", "", ref)

    # Extract path and fragment
    if "#" in ref:
        path_part, fragment = ref.split("#", 1)
    else:
        path_part, fragment = ref, ""

    # Normalize file path
    clean_path = Path(path_part).resolve().as_posix()
    clean_path = re.sub(r".*components/", "components/", clean_path)

    # Normalize JSON pointer fragment
    frag_parts = fragment.strip("/").split("/")
    if "components" in frag_parts:
        try:
            idx = frag_parts.index("components")
            component_type = frag_parts[idx + 1]
            component_name = frag_parts[idx + 2]
            return f"{clean_path}#/components/{component_type}/{component_name}"
        except IndexError:
            pass

    return ref

def fix_and_clean_refs(obj, filepath):
    changed = False
    if isinstance(obj, dict):
        keys_to_delete = []
        for k, v in obj.items():
            if k == "$ref":
                if v.endswith("#/components/../components"):
                    print(f"❌ Removed broken $ref in {filepath}: {v}")
                    keys_to_delete.append(k)
                    changed = True
                else:
                    fixed = normalize_modular_ref(v)
                    if fixed != v:
                        obj[k] = fixed
                        changed = True
            else:
                changed |= fix_and_clean_refs(v, filepath)
        for k in keys_to_delete:
            del obj[k]
    elif isinstance(obj, list):
        for item in obj:
            changed |= fix_and_clean_refs(item, filepath)
    return changed

def fix_modular_file(filepath: Path):
    with filepath.open("r", encoding="utf-8") as f:
        content = yaml.safe_load(f)

    if not content:
        return

    if fix_and_clean_refs(content, filepath):
        with filepath.open("w", encoding="utf-8") as f:
            yaml.safe_dump(content, f, sort_keys=False, allow_unicode=True)
        print(f"✅ Cleaned modular file: {filepath}")

def walk_modular():
    for root, _, files in os.walk(MODULAR_ROOT):
        for file in files:
            if file.endswith((".yaml", ".yml")):
                fix_modular_file(Path(root) / file)

if __name__ == "__main__":
    walk_modular()
