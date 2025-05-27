from clio_client.client import Client
from clio_client.api.activities.activitycreate import sync_detailed
from clio_client.api.activities.activitydestroy import sync_detailed
from clio_client.api.activities.activityindex import sync_detailed
from clio_client.api.activities.activityshow import sync_detailed
from clio_client.api.activities.activityupdate import sync_detailed

class ActivitiesApi:
    def __init__(self, client: Client):
        self.client = client

    def activitycreate(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def activitydestroy(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def activityindex(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def activityshow(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def activityupdate(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)
