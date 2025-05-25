import yaml
import os

ROOT_FILE = "./openapi/root.yaml"

OAUTH2_SECURITY = {
    "oauth2": {
        "type": "oauth2",
        "flows": {
            "clientCredentials": {
                "tokenUrl": "https://app.clio.com/oauth/token",
                "scopes": {
                    "read:matters": "Read matters",
                    "write:matters": "Modify matters"
                }
            }
        }
    }
}

GLOBAL_SECURITY = [
    {"oauth2": ["read:matters", "write:matters"]}
]

def patch_root_security():
    if not os.path.exists(ROOT_FILE):
        print("❌ root.yaml not found.")
        return

    with open(ROOT_FILE, "r") as f:
        spec = yaml.safe_load(f)

    modified = False

    if "components" not in spec:
        spec["components"] = {}
    if "securitySchemes" not in spec["components"]:
        spec["components"]["securitySchemes"] = OAUTH2_SECURITY
        modified = True
    elif "oauth2" not in spec["components"]["securitySchemes"]:
        spec["components"]["securitySchemes"]["oauth2"] = OAUTH2_SECURITY["oauth2"]
        modified = True

    if "security" not in spec:
        spec["security"] = GLOBAL_SECURITY
        modified = True

    if modified:
        with open(ROOT_FILE, "w") as f:
            yaml.dump(spec, f, sort_keys=False)
        print("✅ OAuth2 security scheme and global security added to root.yaml")
    else:
        print("ℹ️ root.yaml already contains security info — no changes made.")

if __name__ == "__main__":
    patch_root_security()
