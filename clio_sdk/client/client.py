from httpx import AsyncClient


class ClioClient:
    def __init__(self, token: str, base_url: str = "https://app.clio.com/api/v4"):
        self.token = token
        self.base_url = base_url
        self.client = AsyncClient(base_url=self.base_url, headers=self._headers())

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