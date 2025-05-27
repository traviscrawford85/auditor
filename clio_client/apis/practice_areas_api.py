from clio_client.client import Client
from clio_client.api.practice_areas.practice_areacreate import sync_detailed
from clio_client.api.practice_areas.practice_areadestroy import sync_detailed
from clio_client.api.practice_areas.practice_areaindex import sync_detailed
from clio_client.api.practice_areas.practice_areashow import sync_detailed
from clio_client.api.practice_areas.practice_areaupdate import sync_detailed

class PracticeAreasApi:
    def __init__(self, client: Client):
        self.client = client

    def practice_areacreate(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def practice_areadestroy(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def practice_areaindex(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def how(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def practice_areaupdate(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)
