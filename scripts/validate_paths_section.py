import sys
import yaml

spec_path = "openapi/expanded_full.yaml"

with open(spec_path, "r") as f:
    spec = yaml.safe_load(f)

if "paths" not in spec or not isinstance(spec["paths"], dict):
    print("❌ ERROR: The OpenAPI spec is missing a valid 'paths:' section.")
    sys.exit(1)

if not spec["paths"]:
    print("❌ ERROR: The 'paths:' section is empty. No endpoints defined.")
    sys.exit(1)

print("✅ 'paths:' section exists and contains endpoints.")