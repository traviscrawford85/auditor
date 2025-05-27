from clio_client.client import Client
from clio_client.api.users.userindex import sync_detailed
from clio_client.api.users.usershow import sync_detailed
from clio_client.api.users.userwho_am_i import sync_detailed

class UsersApi:
    def __init__(self, client: Client):
        self.client = client

    def userindex(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def how(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def userwho_am_i(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)
