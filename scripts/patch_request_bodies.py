from pathlib import Path
import yaml

REQUEST_BODIES_DIR = Path("openapi/components/requestBodies")

def patch_request_bodies():
    for file in REQUEST_BODIES_DIR.glob("*.yaml"):
        with file.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}

        if not isinstance(data, dict) or len(data) != 1:
            print(f"❌ Invalid format in {file.name} (expected one top-level key)")
            continue

        top_key = next(iter(data))
        body = data[top_key]

        if not isinstance(body, dict):
            print(f"❌ Top-level value under {top_key} is not a dict in {file.name}")
            continue

        if "content" not in body or not isinstance(body["content"], dict):
            print(f"⚠️ Missing or invalid 'content' field in {file.name} under {top_key}")
        else:
            print(f"✔️ Valid: {file.name}")

patch_request_bodies()
