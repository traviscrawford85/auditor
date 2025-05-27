from clio_client.client import Client
from clio_client.api.notes.notecreate import sync_detailed
from clio_client.api.notes.notedestroy import sync_detailed
from clio_client.api.notes.noteindex import sync_detailed
from clio_client.api.notes.noteshow import sync_detailed
from clio_client.api.notes.noteupdate import sync_detailed

class NotesApi:
    def __init__(self, client: Client):
        self.client = client

    def notecreate(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def notedestroy(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def noteindex(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def how(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def noteupdate(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)
