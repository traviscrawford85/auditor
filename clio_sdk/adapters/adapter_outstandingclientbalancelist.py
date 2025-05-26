# Adapter for outstandingclientbalancelist
from clio_sdk.models.outstandingclientbalancelist import OutstandingclientbalancelistIn, OutstandingclientbalancelistOut, OutstandingclientbalancelistUpdate, OutstandingclientbalancelistDb
from clio_client.models.outstanding_client_balance_list import OutstandingClientBalanceList

def convert_sdk_to_outstandingclientbalancelistout(src: OutstandingClientBalanceList) -> OutstandingclientbalancelistOut:
    """Converts a clio_client model to clio_sdk model."""
    return OutstandingclientbalancelistOut(**src.model_dump())

def convert_outstandingclientbalancelistin_to_sdk(src: OutstandingclientbalancelistIn) -> OutstandingClientBalanceList:
    """Converts a clio_sdk model to clio_client model."""
    return OutstandingClientBalanceList(**src.model_dump())
