# Adapter for lienbase
from clio_sdk.models.lienbase import LienbaseIn, LienbaseOut, LienbaseUpdate, LienbaseDb
from clio_client.models import client

def convert_sdk_to_lienbaseout(src: client) -> LienbaseOut:
    return LienbaseOut(**src.dict())

def convert_lienbasein_to_sdk(src: LienbaseIn) -> client:
    return client(**src.dict())
