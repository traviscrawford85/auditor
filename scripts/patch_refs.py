from pathlib import Path

import yaml

OPENAPI_DIR = Path('openapi')
COMPONENTS_DIR = 'components'

def patch_refs_in_file(file_path):
    rel_path = file_path.relative_to(OPENAPI_DIR)
    parent_dir = rel_path.parent

    with open(file_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)

    def patch_refs(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == '$ref' and isinstance(value, str):
                    if value.startswith('./components/'):
                        obj[key] = f'../components/{value.split("./components/")[1]}'
                else:
                    patch_refs(value)
        elif isinstance(obj, list):
            for item in obj:
                patch_refs(item)

    patch_refs(data)

    # Backup original file
    backup_file = file_path.with_suffix('.yaml.bak')
    file_path.rename(backup_file)

    # Write updated file
    with open(file_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, sort_keys=False)

    print(f"✅ Patched refs in {file_path} (backup saved as {backup_file.name})")

def main():
    yaml_files = list((OPENAPI_DIR / 'paths').rglob('*.yaml'))
    if not yaml_files:
        print("⚠️ No YAML files found under openapi/paths/")
        return

    for file_path in yaml_files:
        patch_refs_in_file(file_path)

    print("🎉 All refs patched across openapi/paths/*.yaml")

if __name__ == '__main__':
    main()
