# Adapter for clientportalbase
from clio_sdk.models.clientportalbase import ClientportalbaseIn, ClientportalbaseOut, ClientportalbaseUpdate, ClientportalbaseDb
from clio_client.models import client_portal_base

def convert_sdk_to_clientportalbaseout(src: client_portal_base) -> ClientportalbaseOut:
    return ClientportalbaseOut(**src.dict())

def convert_clientportalbasein_to_sdk(src: ClientportalbaseIn) -> client_portal_base:
    return client_portal_base(**src.dict())
