# Adapter for trustrequestbase
from clio_sdk.models.trustrequestbase import TrustrequestbaseIn, TrustrequestbaseOut, TrustrequestbaseUpdate, TrustrequestbaseDb
from clio_client.models import trust_request

def convert_sdk_to_trustrequestbaseout(src: trust_request) -> TrustrequestbaseOut:
    return TrustrequestbaseOut(**src.dict())

def convert_trustrequestbasein_to_sdk(src: TrustrequestbaseIn) -> trust_request:
    return trust_request(**src.dict())
