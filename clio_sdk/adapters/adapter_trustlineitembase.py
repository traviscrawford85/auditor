# Adapter for trustlineitembase
from clio_sdk.models.trustlineitembase import TrustlineitembaseIn, TrustlineitembaseOut, TrustlineitembaseUpdate, TrustlineitembaseDb
from clio_client.models import trust_line_item

def convert_sdk_to_trustlineitembaseout(src: trust_line_item) -> TrustlineitembaseOut:
    return TrustlineitembaseOut(**src.dict())

def convert_trustlineitembasein_to_sdk(src: TrustlineitembaseIn) -> trust_line_item:
    return trust_line_item(**src.dict())
