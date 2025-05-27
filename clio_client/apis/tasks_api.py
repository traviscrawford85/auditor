from clio_client.client import Client
from clio_client.api.tasks.taskcreate import sync_detailed
from clio_client.api.tasks.taskdestroy import sync_detailed
from clio_client.api.tasks.taskindex import sync_detailed
from clio_client.api.tasks.taskshow import sync_detailed
from clio_client.api.tasks.taskupdate import sync_detailed

class TasksApi:
    def __init__(self, client: Client):
        self.client = client

    def taskcreate(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def taskdestroy(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def taskindex(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def how(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)

    def taskupdate(self, *args, **kwargs):
        return sync_detailed(client=self.client, *args, **kwargs)
