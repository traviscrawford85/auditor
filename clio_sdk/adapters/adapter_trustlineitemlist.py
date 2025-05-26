# Adapter for trustlineitemlist
from clio_sdk.models.trustlineitemlist import TrustlineitemlistIn, TrustlineitemlistOut, TrustlineitemlistUpdate, TrustlineitemlistDb
from clio_client.models import trust_line_item_list

def convert_sdk_to_trustlineitemlistout(src: trust_line_item_list) -> TrustlineitemlistOut:
    return TrustlineitemlistOut(**src.dict())

def convert_trustlineitemlistin_to_sdk(src: TrustlineitemlistIn) -> trust_line_item_list:
    return trust_line_item_list(**src.dict())
