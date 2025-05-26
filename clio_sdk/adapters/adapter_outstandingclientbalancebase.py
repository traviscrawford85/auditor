# Adapter for outstandingclientbalancebase
from clio_sdk.models.outstandingclientbalancebase import OutstandingclientbalancebaseIn, OutstandingclientbalancebaseOut, OutstandingclientbalancebaseUpdate, OutstandingclientbalancebaseDb
from clio_client.models import outstanding_client_balance

def convert_sdk_to_outstandingclientbalancebaseout(src: outstanding_client_balance) -> OutstandingclientbalancebaseOut:
    return OutstandingclientbalancebaseOut(**src.dict())

def convert_outstandingclientbalancebasein_to_sdk(src: OutstandingclientbalancebaseIn) -> outstanding_client_balance:
    return outstanding_client_balance(**src.dict())
