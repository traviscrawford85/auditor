from clio_client.client import Client
from clio_client.api.matters.mattercreate import sync_detailed
from clio_client.api.matters.matterdestroy import sync_detailed
from clio_client.api.matters.matterindex import sync_detailed
from clio_client.api.matters.mattershow import sync_detailed
from clio_client.api.matters.matterupdate import sync_detailed

class MattersApi:
    def __init__(self, client: Client):
        self.client = client

    def mattercreate(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def matterdestroy(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def matterindex(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def how(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def matterupdate(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)
