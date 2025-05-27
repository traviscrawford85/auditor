from pathlib import Path

import yaml

BASE_DIR = Path("openapi")
PARAMS_FILE = BASE_DIR / "components" / "parameters.yaml"
RESPONSES_FILE = BASE_DIR / "components" / "responses.yaml"
REQUEST_BODIES_FILE = BASE_DIR / "components" / "requestBodies.yaml"

def load_component_refs(file_path, component_type):
    if not file_path.exists():
        return {}
    with file_path.open("r", encoding="utf-8") as f:
        content = yaml.safe_load(f)
    return {
        key: f"components/{file_path.name}#/components/{component_type}/{key}"
        for key in content.get("components", {}).get(component_type, {})
    }

parameters = load_component_refs(PARAMS_FILE, "parameters")
responses = load_component_refs(RESPONSES_FILE, "responses")
request_bodies = load_component_refs(REQUEST_BODIES_FILE, "requestBodies")

COMMON_PARAMS = ["X-API-VERSION", "id"]
COMMON_RESPONSES = ["200_Ok", "304_Not_Modified", "400_Bad_Request", "401_Unauthorized", "403_Forbidden", "404_Not_Found", "429_Too_Many_Requests"]
PATCH_RESPONSES = COMMON_RESPONSES + ["412_Precondition_Failed", "422_Unprocessable_Entity"]
DELETE_RESPONSES = ["204_No_Content", "403_Forbidden"]

def dedupe_and_clean(details, key):
    if key not in details:
        return
    if isinstance(details[key], list):
        refs = [p.get("$ref") for p in details[key] if isinstance(p, dict) and p.get("$ref")]
        unique_refs = []
        seen = set()
        for ref in refs:
            if ref and ref not in seen:
                unique_refs.append({"$ref": ref})
                seen.add(ref)
        if unique_refs:
            details[key] = unique_refs
        else:
            del details[key]
    elif isinstance(details[key], dict):
        new_map = {}
        seen = set()
        for k, v in details[key].items():
            if isinstance(v, dict) and "$ref" in v and v["$ref"] not in seen:
                new_map[k] = v
                seen.add(v["$ref"])
        if new_map:
            details[key] = new_map
        else:
            del details[key]

def normalize_and_patch(file_path: Path):
    with file_path.open("r", encoding="utf-8") as f:
        content = yaml.safe_load(f)

    if not content:
        return

    changed = False
    for path_key, methods in content.items():
        if not isinstance(methods, dict):
            continue
        for method, details in methods.items():
            if not isinstance(details, dict):
                continue

            for key in ["parameters", "responses", "requestBody"]:
                if key in details and isinstance(details[key], dict) and "parameters" in details[key]:
                    # clear out nested duplications like responses.parameters etc.
                    del details[key]["parameters"]
                    changed = True
                if key in details and isinstance(details[key], dict) and "responses" in details[key]:
                    del details[key]["responses"]
                    changed = True

            dedupe_and_clean(details, "parameters")
            dedupe_and_clean(details, "responses")

            if "parameters" not in details:
                details["parameters"] = [{"$ref": parameters[p]} for p in COMMON_PARAMS if p in parameters]
                changed = True

            if "responses" not in details:
                details["responses"] = {}
                ref_list = PATCH_RESPONSES if method == "patch" else DELETE_RESPONSES if method == "delete" else COMMON_RESPONSES
                for r in ref_list:
                    if r in responses:
                        code = r.split("_")[0]
                        details["responses"][code] = {"$ref": responses[r]}
                        changed = True

            if method == "patch" and "requestBody" not in details:
                body_ref = next(iter(request_bodies.values()), None)
                if body_ref:
                    details["requestBody"] = {"$ref": body_ref}
                    changed = True

    if changed:
        with file_path.open("w", encoding="utf-8") as f:
            yaml.safe_dump(content, f, sort_keys=False)
        print(f"✅ Cleaned and patched: {file_path.name}")

paths_dir = BASE_DIR / "paths"
for file in paths_dir.glob("*.yaml"):
    normalize_and_patch(file)
