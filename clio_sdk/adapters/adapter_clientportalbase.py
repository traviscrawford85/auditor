# Adapter for clientportalbase
from clio_sdk.models.clientportalbase import ClientportalBaseIn, ClientportalbaseOut, ClientportalbaseUpdate, ClientportalbaseDb
from clio_client.models.client_portal_base import ClientPortalBase

def convert_sdk_to_clientportalbaseout(src: ClientPortalBase) -> ClientportalbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ClientportalbaseOut(**src.model_dump())

def convert_clientportalbasein_to_sdk(src: ClientportalBaseIn) -> ClientPortalBase:
    """Converts a clio_sdk model to clio_client model."""
    return ClientPortalBase(**src.model_dump())
