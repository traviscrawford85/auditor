import os

OPENAPI_ROOT = "./openapi"
COPILOT_PROMPT = """\
# copilot-audit: true
# Description: This file is a modular part of a larger OpenAPI specification for a Clio API integration.
# Objective: Audit this spec segment for completeness, correctness, and consistency with OpenAPI 3.1 standards.
# Tasks:
# 1. Verify valid OpenAPI syntax (YAML structure, keys).
# 2. Confirm all `$ref` targets exist and are reachable (local or shared component references).
# 3. Ensure operationId values are unique, descriptive, and follow the {method}_{resource} pattern.
# 4. Check that requestBody and response schemas use proper `$ref`s and avoid inline duplication.
# 5. Validate that all schemas and components are named clearly and represent their intent.
# 6. Detect and flag unused components under `components.schemas`, `components.responses`, etc.
# 7. Review tag usage for clarity, grouping, and alignment with x-tagGroups (if used).
# 8. Enforce use of standard HTTP methods and response codes (e.g., 200, 201, 400, 404, 422, 500).
# 9. Validate pagination, filtering, and sorting patterns for list endpoints.
# 10. Check that the top-level spec (if root) defines: openapi version, info, servers, paths, components, and tags.
# 11. Ensure every schema property has a `type` and if applicable a `format`; infer missing types where possible.
# 12. Recommend stronger type hints (e.g., `integer` vs `string`, `date-time` vs `string`) where obvious.
# Output:
# - A checklist of errors or improvements, preferably with line references.
# - Suggestions for how to fix or improve structure, naming, reuse, and typing.
#
# NOTE: This file is part of a spec intended to generate a custom Python client using `openapi-python-client`,
# which expects well-formed operationIds and `$ref`s to derive method names and models.
"""

def check_prompt_in_file(filepath: str) -> bool:
    with open(filepath, "r", encoding="utf-8") as f:
        return COPILOT_PROMPT.strip().splitlines()[0] in f.read()

def prepend_prompt_to_yaml_files():
    for subdir, _, files in os.walk(OPENAPI_ROOT):
        for file in files:
            if file.endswith((".yaml", ".yml")):
                path = os.path.join(subdir, file)
                if not check_prompt_in_file(path):
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                    with open(path, "w", encoding="utf-8") as fw:
                        fw.write(COPILOT_PROMPT + "\n" + content)
                    print(f"Prepended prompt to: {path}")

if __name__ == "__main__":
    prepend_prompt_to_yaml_files()
    print("Copilot prompt prepended to all YAML files where it was missing.")
