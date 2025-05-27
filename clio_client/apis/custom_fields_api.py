from clio_client.client import Client
from clio_client.api.custom_fields.custom_fieldcreate import sync_detailed
from clio_client.api.custom_fields.custom_fielddestroy import sync_detailed
from clio_client.api.custom_fields.custom_fieldindex import sync_detailed
from clio_client.api.custom_fields.custom_fieldshow import sync_detailed
from clio_client.api.custom_fields.custom_fieldupdate import sync_detailed

class CustomFieldsApi:
    def __init__(self, client: Client):
        self.client = client

    def custom_fieldcreate(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def custom_fielddestroy(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def custom_fieldindex(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def how(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def custom_fieldupdate(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)
