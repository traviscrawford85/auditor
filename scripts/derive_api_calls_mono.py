import yaml
import pandas as pd

OPENAPI_FILE = "openapi/openapi_final_cleaned.yaml"

def load_openapi(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def resolve_ref(ref, components):
    try:
        if ref.startswith("#/components/parameters/"):
            name = ref.split("/")[-1]
            return components.get("parameters", {}).get(name, {})
        elif ref.startswith("#/components/requestBodies/"):
            name = ref.split("/")[-1]
            return components.get("requestBodies", {}).get(name, {})
    except Exception:
        return {}
    return {}

def parse_paths(openapi):
    components = openapi.get("components", {})
    data = []
    for path, methods in openapi.get("paths", {}).items():
        for method, details in methods.items():
            if method not in ['get', 'post', 'put', 'patch', 'delete']:
                continue
            summary = details.get("summary", "")
            desc = details.get("description", "")
            op_id = details.get("operationId", "")
            request_body_ref = details.get("requestBody", {}).get("$ref")
            request_schema = resolve_ref(request_body_ref, components).get("description") if request_body_ref else None
            param_summaries = []
            for param in details.get("parameters", []):
                if isinstance(param, dict) and "$ref" in param:
                    resolved = resolve_ref(param["$ref"], components)
                    if resolved:
                        param_summaries.append(resolved.get("name", ""))
            data.append({
                "Path": path,
                "Method": method.upper(),
                "OperationId": op_id,
                "Summary": summary,
                "Description": desc,
                "Request Schema": request_schema,
                "Query Params": ", ".join(param_summaries)
            })
    return pd.DataFrame(data)

if __name__ == "__main__":
    openapi = load_openapi(OPENAPI_FILE)
    df = parse_paths(openapi)
    df.to_csv("api_call_summary.csv", index=False)
    print("✅ API call summary saved to api_call_summary.csv")
