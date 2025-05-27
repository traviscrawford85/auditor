from clio_client.client import Client
from clio_client.api.contacts.contactcreate import sync_detailed
from clio_client.api.contacts.contactdestroy import sync_detailed
from clio_client.api.contacts.contactindex import sync_detailed
from clio_client.api.contacts.contactshow import sync_detailed
from clio_client.api.contacts.contactupdate import sync_detailed

class ContactsApi:
    def __init__(self, client: Client):
        self.client = client

    def contactcreate(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def contactdestroy(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def contactindex(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def how(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def contactupdate(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)
