from clio_client.client import Client
from clio_client.api.clients.clientshow import sync_detailed

class ClientsApi:
    def __init__(self, client: Client):
        self.client = client

    def how(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)
