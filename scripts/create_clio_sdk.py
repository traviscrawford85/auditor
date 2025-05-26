import os
from pathlib import Path

# Scaffold a directory structure for a Clio-aware integration layer
base_dir = Path("/clio_sdk")
dirs_to_create = [
    base_dir,
    base_dir / "models",
    base_dir / "queries",
    base_dir / "client",
    base_dir / "utils"
]

# Create folders
for d in dirs_to_create:
    os.makedirs(d, exist_ok=True)

# Seed basic __init__.py files
for d in dirs_to_create:
    (d / "__init__.py").touch()

# Create a sample client wrapper
client_code = '''
from httpx import AsyncClient

class ClioClient:
    def __init__(self, token: str, base_url: str = "https://app.clio.com/api/v4"):
        self.token = token
        self.base_url = base_url
        self.client = AsyncClient(base_url=self.base_url, headers=self._headers)

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
        }

    async def get(self, path: str, params: dict = None):
        resp = await self.client.get(path, params=params)
        resp.raise_for_status()
        return resp.json()

    async def post(self, path: str, data: dict = None):
        resp = await self.client.post(path, json=data)
        resp.raise_for_status()
        return resp.json()

    async def close(self):
        await self.client.aclose()
'''

with open(base_dir / "client" / "client.py", "w") as f:
    f.write(client_code.strip())

# Create README with structure explanation
readme_text = '''
# Clio SDK Scaffold

This is a customizable Python SDK for Clio, tailored to your firm's needs.

## Structure

- `models/`: Pydantic models generated from OpenAPI or refined manually
- `client/`: Authenticated HTTP client with rate limiting and retries
- `queries/`: Reusable query builders for complex operations (e.g., joining Matters + Tasks)
- `utils/`: Helpers for date logic, pagination, batching, etc.

Run `openapi-python-client generate --path openapi_final_cleaned.yaml --config config.json` to generate models in `models/`.

'''

with open(base_dir / "README.md", "w") as f:
    f.write(readme_text.strip())

str(base_dir)
