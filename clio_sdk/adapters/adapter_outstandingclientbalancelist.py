# Adapter for outstandingclientbalancelist
from clio_sdk.models.outstandingclientbalancelist import OutstandingclientbalancelistIn, OutstandingclientbalancelistOut, OutstandingclientbalancelistUpdate, OutstandingclientbalancelistDb
from clio_client.models import outstanding_client_balance_list

def convert_sdk_to_outstandingclientbalancelistout(src: outstanding_client_balance_list) -> OutstandingclientbalancelistOut:
    return OutstandingclientbalancelistOut(**src.dict())

def convert_outstandingclientbalancelistin_to_sdk(src: OutstandingclientbalancelistIn) -> outstanding_client_balance_list:
    return outstanding_client_balance_list(**src.dict())
