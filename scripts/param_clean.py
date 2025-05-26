from pathlib import Path
import yaml

BASE_DIR = Path("]openapi")
paths_dir = BASE_DIR / "paths"

def clean_duplicate_sections(file_path: Path):
    with file_path.open("r", encoding="utf-8") as f:
        content = yaml.safe_load(f)

    if not content:
        return

    changed = False
    for path_key, methods in content.items():
        if not isinstance(methods, dict):
            continue
        for method, details in methods.items():
            if not isinstance(details, dict):
                continue

            keys_to_remove = []
            for k, v in details.items():
                if k in ["parameters", "responses"] and isinstance(v, (list, dict)):
                    if isinstance(v, list) and all(not item for item in v):
                        keys_to_remove.append(k)
                    elif isinstance(v, dict) and all(not val for val in v.values()):
                        keys_to_remove.append(k)

            for k in keys_to_remove:
                del details[k]
                changed = True

    if changed:
        with file_path.open("w", encoding="utf-8") as f:
            yaml.safe_dump(content, f, sort_keys=False)
        print(f"🧹 Removed duplicates/empties: {file_path.name}")

# Apply to all files in the paths directory
for path_file in paths_dir.glob("*.yaml"):
    clean_duplicate_sections(path_file)
