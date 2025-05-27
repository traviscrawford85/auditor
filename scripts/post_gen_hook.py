import os
from pathlib import Path
import re

ROOT = Path("clio_client/api")
DOMAINS = [
    "tasks",
    "matters",
    "contacts",
    "clients",
    "calendar_entries",
    "documents",
    "notes",
    "custom_fields",
    "practice_areas",
    "users",
    "activities",
]

API_DIR = Path("clio_client/apis")
API_DIR.mkdir(parents=True, exist_ok=True)

def extract_function_name(file_path: Path):
    content = file_path.read_text()
    match = re.search(r'def (sync|asyncio)(_detailed)?\(', content)
    if match:
        return file_path.stem, match.group(0).split(' ')[1].split('(')[0]
    return None, None

def build_api_class(domain: str):
    domain_path = ROOT / domain
    output_file = API_DIR / f"{domain}_api.py"
    class_name = f"{''.join(w.capitalize() for w in domain.split('_'))}Api"

    import_lines = ["from clio_client.client import Client"]
    method_defs = []

    for file in sorted(domain_path.glob("*.py")):
        if file.name.startswith("__") or not file.suffix == ".py":
            continue

        module_name, func_name = extract_function_name(file)
        if not func_name:
            continue

        import_lines.append(f"from clio_client.api.{domain}.{module_name} import {func_name}")
        method_name = module_name.replace(domain, "", 1).replace("_", " ").strip().replace(" ", "_")

        method_defs.append(f"""    def {method_name}(self, *args, **kwargs):
        return {func_name}(client=self.client, *args, **kwargs)
""")

    class_code = "\n".join([
        *import_lines,
        "",
        f"class {class_name}:",
        "    def __init__(self, client: Client):",
        "        self.client = client",
        "",
        *method_defs,
    ])

    output_file.write_text(class_code.strip() + "\n")
    print(f"✅ Generated {output_file}")

def main():
    for domain in DOMAINS:
        build_api_class(domain)

if __name__ == "__main__":
    main()
