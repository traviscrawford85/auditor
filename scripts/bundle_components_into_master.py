from pathlib import Path

import yaml

BASE_DIR = Path("openapi/components")
SECTIONS = ["schemas", "parameters", "responses", "requestBodies"]
SECTION_FILES = {s: BASE_DIR / f"{s}.yaml" for s in SECTIONS}
MASTER_COMPONENTS = Path("openapi/components.yaml")

def load_section(path):
    if not path.exists():
        print(f"⚠️ Missing section file: {path}")
        return {}
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
        return data.get("components", {}).get(path.stem, {})

def main():
    master = {"components": {}}
    for section, file_path in SECTION_FILES.items():
        print(f"📦 Loading {section} from {file_path}")
        master["components"][section] = load_section(file_path)

    MASTER_COMPONENTS.parent.mkdir(parents=True, exist_ok=True)
    with MASTER_COMPONENTS.open("w", encoding="utf-8") as f:
        yaml.safe_dump(master, f, sort_keys=False)
    print(f"\n✅ Created master components bundle: {MASTER_COMPONENTS}")

if __name__ == "__main__":
    main()
