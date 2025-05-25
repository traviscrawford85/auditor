import yaml

ROOT_FILE = "./openapi/root.yaml"

def dedupe_tags():
    with open(ROOT_FILE, "r") as f:
        spec = yaml.safe_load(f)

    if "tags" not in spec:
        print("No tags found.")
        return

    seen = set()
    deduped = []
    for tag in spec["tags"]:
        name = tag.get("name")
        if name not in seen:
            deduped.append(tag)
            seen.add(name)

    if len(deduped) != len(spec["tags"]):
        spec["tags"] = deduped
        with open(ROOT_FILE, "w") as f:
            yaml.dump(spec, f, sort_keys=False)
        print("✅ Duplicate tags removed from root.yaml")
    else:
        print("ℹ️ No duplicate tags found.")

if __name__ == "__main__":
    dedupe_tags()
