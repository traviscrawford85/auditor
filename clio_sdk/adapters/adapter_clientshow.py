# Adapter for clientshow
from clio_sdk.models.clientshow import ClientshowIn, ClientshowOut, ClientshowUpdate, ClientshowDb
from clio_client.models import client_show

def convert_sdk_to_clientshowout(src: client_show) -> ClientshowOut:
    return ClientshowOut(**src.dict())

def convert_clientshowin_to_sdk(src: ClientshowIn) -> client_show:
    return client_show(**src.dict())
