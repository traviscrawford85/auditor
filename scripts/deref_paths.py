import argparse
from pathlib import Path

import yaml


def load_spec(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def save_spec(data: dict, path: Path):
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False)

def resolve_ref(ref: str, components: dict) -> dict:
    if not ref.startswith("#/components/"):
        return {"$ref": ref}
    _, _, path = ref.partition("#/components/")
    section, _, name = path.partition("/")
    return components.get(section, {}).get(name, {"$ref": ref})

def deref_node(node, components):
    if isinstance(node, dict):
        if "$ref" in node:
            resolved = resolve_ref(node["$ref"], components)
            merged = {**resolved, **{k: v for k, v in node.items() if k != "$ref"}}
            return deref_node(merged, components)
        return {k: deref_node(v, components) for k, v in node.items()}
    elif isinstance(node, list):
        return [deref_node(i, components) for i in node]
    return node

def main():
    parser = argparse.ArgumentParser(description="Deep dereference all $refs in OpenAPI paths and components")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    spec = load_spec(args.input)
    components = spec.get("components", {})

    for path, methods in spec.get("paths", {}).items():
        for method, op in methods.items():
            if isinstance(op, dict):
                for field in ("parameters", "requestBody", "responses"):
                    if field in op:
                        op[field] = deref_node(op[field], components)

    save_spec(spec, args.output)
    print(f"✅ Dereferenced spec saved to → {args.output}")

if __name__ == "__main__":
    main()
