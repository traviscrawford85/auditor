from clio_client.client import Client
from clio_client.api.calendar_entries.calendar_entrycreate import sync_detailed
from clio_client.api.calendar_entries.calendar_entrydestroy import sync_detailed
from clio_client.api.calendar_entries.calendar_entryindex import sync_detailed
from clio_client.api.calendar_entries.calendar_entryshow import sync_detailed
from clio_client.api.calendar_entries.calendar_entryupdate import sync_detailed

class CalendarEntriesApi:
    def __init__(self, client: Client):
        self.client = client

    def calendar_entrycreate(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def calendar_entrydestroy(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def calendar_entryindex(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def calendar_entryshow(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def calendar_entryupdate(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)
