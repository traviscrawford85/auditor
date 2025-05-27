from clio_client.client import Client
from clio_client.api.documents.documentcopy import sync_detailed
from clio_client.api.documents.documentcreate import sync_detailed
from clio_client.api.documents.documentdestroy import sync_detailed
from clio_client.api.documents.documentdownload import sync_detailed
from clio_client.api.documents.documentindex import sync_detailed
from clio_client.api.documents.documentshow import sync_detailed
from clio_client.api.documents.documentupdate import sync_detailed

class DocumentsApi:
    def __init__(self, client: Client):
        self.client = client

    def documentcopy(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def documentcreate(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def documentdestroy(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def documentdownload(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def documentindex(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def how(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def documentupdate(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)
