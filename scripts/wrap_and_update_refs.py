from pathlib import Path
from urllib.parse import urlparse

import yaml


def wrap_files(input_dir: str, output_file: str, section_name: str):
    combined = {}
    input_path = Path(input_dir)
    refs = []

    for file in input_path.glob('*.yaml'):  # Change to rglob for recursive
        if file.name == 'rename_map.yaml':
            print(f"⚠️ Skipping rename_map → {file}")
            continue
        try:
            key = file.stem
            with file.open('r', encoding='utf-8') as f:
                content = yaml.safe_load(f) or {}
                refs.extend(extract_refs(content, base_path=file))
            combined[key] = content
        except yaml.YAMLError as e:
            print(f"❌ Failed to load YAML: {file} → {e}")
        except Exception as e:
            print(f"❌ Error processing file {file}: {e}")

    wrapped = {'components': {section_name: combined}}

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open('w', encoding='utf-8') as f:
        yaml.dump(wrapped, f, sort_keys=False)
    print(f"✅ Merged and wrapped → {output_file}")

    # Validate $refs
    check_refs(refs)


def extract_refs(node, base_path: Path):
    """Recursively extract $ref values from a YAML structure."""
    refs = []
    if isinstance(node, dict):
        for k, v in node.items():
            if k == '$ref' and isinstance(v, str):
                refs.append((v, base_path))
            else:
                refs.extend(extract_refs(v, base_path))
    elif isinstance(node, list):
        for item in node:
            refs.extend(extract_refs(item, base_path))
    return refs


def check_refs(refs):
    print("🔍 Validating $ref targets...")

    alt_paths = [
        Path("openapi/components/schemas/bases"),
        Path("openapi/shared/schemas")
    ]

    for ref, base in refs:
        parsed = urlparse(ref)
        if parsed.scheme or parsed.netloc:
            print(f"ℹ️ Skipping external ref: {ref}")
            continue

        if ref.startswith('#'):
            continue

        parts = ref.split('#')
        file_part = parts[0]
        fragment = parts[1] if len(parts) > 1 else None

        ref_path = (base.parent / file_part).resolve()
        if not ref_path.exists():
            # Try alternate directories
            for alt_base in alt_paths:
                candidate = (alt_base / Path(file_part).name).resolve()
                if candidate.exists():
                    ref_path = candidate
                    break
            else:
                print(f"❌ Missing ref file: {ref} → resolved to {ref_path}")
                continue

        if fragment:
            try:
                with ref_path.open('r', encoding='utf-8') as f:
                    target_yaml = yaml.safe_load(f)
                keys = fragment.lstrip('/').split('/')
                for key in keys:
                    target_yaml = target_yaml[key]
            except Exception as e:
                print(f"❌ Invalid ref fragment {ref} → {e}")
                continue

        print(f"✅ Resolved: {ref}")


if __name__ == "__main__":
    sections = ['schemas', 'parameters', 'responses', 'requestBodies']
    for section in sections:
        input_dir = f'openapi/components/{section}'
        output_file = f'openapi/components/{section}.yaml'
        wrap_files(input_dir, output_file, section)
