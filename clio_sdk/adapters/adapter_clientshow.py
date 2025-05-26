# Adapter for clientshow
from clio_sdk.models.clientshow import ClientshowIn, ClientshowOut, ClientshowUpdate, ClientshowDb
from clio_client.models.client_show import ClientShow

def convert_sdk_to_clientshowout(src: ClientShow) -> ClientshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return ClientshowOut(**src.model_dump())

def convert_clientshowin_to_sdk(src: ClientshowIn) -> ClientShow:
    """Converts a clio_sdk model to clio_client model."""
    return ClientShow(**src.model_dump())
