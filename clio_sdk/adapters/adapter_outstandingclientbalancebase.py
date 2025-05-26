# Adapter for outstandingclientbalancebase
from clio_sdk.models.outstandingclientbalancebase import OutstandingclientbalanceBaseIn, OutstandingclientbalancebaseOut, OutstandingclientbalancebaseUpdate, OutstandingclientbalancebaseDb
from clio_client.models.outstanding_client_balance import OutstandingClientBalance

def convert_sdk_to_outstandingclientbalancebaseout(src: OutstandingClientBalance) -> OutstandingclientbalancebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return OutstandingclientbalancebaseOut(**src.model_dump())

def convert_outstandingclientbalancebasein_to_sdk(src: OutstandingclientbalanceBaseIn) -> OutstandingClientBalance:
    """Converts a clio_sdk model to clio_client model."""
    return OutstandingClientBalance(**src.model_dump())
