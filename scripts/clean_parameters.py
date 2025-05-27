from pathlib import Path

import yaml


def clean_parameters(params):
    seen = set()
    cleaned = []
    for p in params:
        if not p or not isinstance(p, dict):
            continue
        ref = p.get("$ref")
        if ref and ref not in seen:
            cleaned.append({"$ref": ref})
            seen.add(ref)
    return cleaned

def clean_responses(responses):
    cleaned = {}
    seen = set()
    for code, resp in responses.items():
        if not resp or not isinstance(resp, dict):
            continue
        ref = resp.get("$ref")
        if ref and ref not in seen:
            cleaned[code] = {"$ref": ref}
            seen.add(ref)
    return cleaned

def clean_file(path_file):
    try:
        with open(path_file, "r", encoding="utf-8") as f:
            content = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"❌ YAML error in {path_file}: {e}")
        return

    if not content or not isinstance(content, dict):
        return

    changed = False
    for path_key, methods in content.items():
        if not isinstance(methods, dict):
            continue
        for method, details in methods.items():
            if not isinstance(details, dict):
                continue

            if "parameters" in details:
                cleaned = clean_parameters(details["parameters"])
                if cleaned != details["parameters"]:
                    details["parameters"] = cleaned
                    changed = True
                if not details["parameters"]:
                    del details["parameters"]
                    changed = True

            if "responses" in details:
                cleaned = clean_responses(details["responses"])
                if cleaned != details["responses"]:
                    details["responses"] = cleaned
                    changed = True
                if not details["responses"]:
                    del details["responses"]
                    changed = True

    if changed:
        with open(path_file, "w", encoding="utf-8") as f:
            yaml.safe_dump(content, f, sort_keys=False)
        print(f"✅ Cleaned: {path_file}")

def main():
    paths_dir = Path("openapi/paths")
    for file in paths_dir.glob("*.yaml"):
        clean_file(file)

if __name__ == "__main__":
    main()
