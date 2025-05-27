from pathlib import Path

import yaml

PATHS_DIR = Path("openapi/paths")

def wrap_path_file(file: Path):
    with file.open("r", encoding="utf-8") as f:
        try:
            content = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"❌ Error in {file.name}: {e}")
            return

    if not isinstance(content, dict):
        print(f"⚠️ Skipping non-dict YAML: {file}")
        return

    top_key = list(content.keys())[0]
    if top_key.startswith("/"):
        print(f"✅ Already wrapped: {file.name}")
        return

    endpoint = "/" + file.stem.replace("_", "/").replace("{/", "{")
    new_content = {endpoint: content}

    with file.open("w", encoding="utf-8") as f:
        yaml.safe_dump(new_content, f, sort_keys=False)

    print(f"🔗 Wrapped: {file.name} → {endpoint}")

def main():
    for file in PATHS_DIR.glob("*.yaml"):
        wrap_path_file(file)

if __name__ == "__main__":
    main()
