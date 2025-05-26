# Adapter for trustlineitembase
from clio_sdk.models.trustlineitembase import TrustlineitemBaseIn, TrustlineitembaseOut, TrustlineitembaseUpdate, TrustlineitembaseDb
from clio_client.models.trust_line_item import TrustLineItem

def convert_sdk_to_trustlineitembaseout(src: TrustLineItem) -> TrustlineitembaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return TrustlineitembaseOut(**src.model_dump())

def convert_trustlineitembasein_to_sdk(src: TrustlineitemBaseIn) -> TrustLineItem:
    """Converts a clio_sdk model to clio_client model."""
    return TrustLineItem(**src.model_dump())
