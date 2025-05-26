# Adapter for clientbase
from clio_sdk.models.clientbase import ClientbaseIn, ClientbaseOut, ClientbaseUpdate, ClientbaseDb
from clio_client.models import client

def convert_sdk_to_clientbaseout(src: client) -> ClientbaseOut:
    return ClientbaseOut(**src.dict())

def convert_clientbasein_to_sdk(src: ClientbaseIn) -> client:
    return client(**src.dict())
