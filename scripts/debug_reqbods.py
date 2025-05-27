import re

import yaml

with open("openapi/components/requestBodies/ReqBody_23c25a8a.yaml") as f:
    doc = yaml.safe_load(f)

if isinstance(doc, dict) and len(doc) == 1:
    # Nested key style
    key, value = next(iter(doc.items()))
    desc = value.get("description", "")
    match = re.search(r"Request Body for ([A-Za-z0-9_]+)", str(desc))
    if match:
        print("✅ Should rename:", key, "→", match.group(1) + "Request")
    else:
        print("❌ No match in description:", desc)
elif isinstance(doc, dict):
    # Flat style (no key wrapper)
    desc = doc.get("description", "")
    match = re.search(r"Request Body for ([A-Za-z0-9_]+)", str(desc))
    if match:
        print("✅ Should rename (based on filename):", match.group(1) + "Request")
    else:
        print("❌ No match in flat description:", desc)
else:
    print("⚠️ Unexpected structure in file")
