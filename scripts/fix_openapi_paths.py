from pathlib import Path

import yaml


def clean_refs(obj, base_path: Path, root_dir: Path):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "$ref" and isinstance(v, str):
                if "#" in v:
                    raw_path, frag = v.split("#", 1)
                    frag = frag.lstrip("/")

                    target_path = (base_path.parent / raw_path).resolve()
                    try:
                        rel_path = target_path.relative_to(root_dir)
                        obj[k] = rel_path.as_posix() + "#/" + frag
                    except ValueError:
                        print(f"❌ Could not resolve ref path: {v} (from {base_path})")
                else:
                    target_path = (base_path.parent / v).resolve()
                    try:
                        rel_path = target_path.relative_to(root_dir)
                        obj[k] = rel_path.as_posix()
                    except ValueError:
                        pass
            else:
                clean_refs(v, base_path, root_dir)
    elif isinstance(obj, list):
        for item in obj:
            clean_refs(item, base_path, root_dir)

def fix_path_file(file_path: Path, output_dir: Path, root_dir: Path):
    with file_path.open("r", encoding="utf-8") as f:
        content = yaml.safe_load(f)

    if content is None:
        return

    if any(m in content for m in ["get", "post", "put", "delete", "patch"]):
        inferred_path = "/" + file_path.stem.replace(".json", "").replace("_", "/")
        content = {inferred_path: content}

    clean_refs(content, base_path=file_path, root_dir=root_dir)

    output_path = output_dir / file_path.name
    with output_path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(content, f, sort_keys=False, allow_unicode=True)
    print(f"✅ Fixed → {file_path.name}")

def bulk_fix_paths(input_dir: str, output_dir: str, root_dir: str):
    in_dir = Path(input_dir)
    out_dir = Path(output_dir)
    root = Path(root_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    for yaml_file in in_dir.glob("*.yaml"):
        fix_path_file(yaml_file, out_dir, root)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Fix OpenAPI path files with ref normalization.")
    parser.add_argument("--input", required=True, help="Input directory of path YAMLs")
    parser.add_argument("--output", required=True, help="Output directory for fixed files")
    parser.add_argument("--root", required=True, help="Root directory of OpenAPI project for relative ref calculation")
    args = parser.parse_args()

    bulk_fix_paths(args.input, args.output, args.root)
