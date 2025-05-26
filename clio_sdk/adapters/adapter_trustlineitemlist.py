# Adapter for trustlineitemlist
from clio_sdk.models.trustlineitemlist import TrustlineitemlistIn, TrustlineitemlistOut, TrustlineitemlistUpdate, TrustlineitemlistDb
from clio_client.models.trust_line_item_list import TrustLineItemList

def convert_sdk_to_trustlineitemlistout(src: TrustLineItemList) -> TrustlineitemlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return TrustlineitemlistOut(**src.model_dump())

def convert_trustlineitemlistin_to_sdk(src: TrustlineitemlistIn) -> TrustLineItemList:
    """Converts a clio_sdk model to clio_client model."""
    return TrustLineItemList(**src.model_dump())
