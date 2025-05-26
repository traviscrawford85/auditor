# Adapter for clientbase
from clio_sdk.models.clientbase import ClientBaseIn, ClientbaseOut, ClientbaseUpdate, ClientbaseDb
from clio_client.models.client import Client

def convert_sdk_to_clientbaseout(src: Client) -> ClientbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ClientbaseOut(**src.model_dump())

def convert_clientbasein_to_sdk(src: ClientBaseIn) -> Client:
    """Converts a clio_sdk model to clio_client model."""
    return Client(**src.model_dump())
