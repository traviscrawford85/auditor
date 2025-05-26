# Adapter for lienbase
from clio_sdk.models.lienbase import LienBaseIn, LienbaseOut, LienbaseUpdate, LienbaseDb
from clio_client.models.client import Client

def convert_sdk_to_lienbaseout(src: Client) -> LienbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return LienbaseOut(**src.model_dump())

def convert_lienbasein_to_sdk(src: LienBaseIn) -> Client:
    """Converts a clio_sdk model to clio_client model."""
    return Client(**src.model_dump())
