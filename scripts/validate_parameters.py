# A script to validate OpenAPI parameters in openapi/components/parameters against the OpenAPI spec.
"""
Validate each parameter in components/parameters/*.yaml to ensure:
- It includes 'name', 'in', and 'schema' fields
- The 'in' field is one of: path, query, header, or cookie
- If 'in' is path, 'required' must be True
- The 'schema' contains a valid 'type'
"""


