# Adapter for trustlineitemshow
from clio_sdk.models.trustlineitemshow import TrustlineitemshowIn, TrustlineitemshowOut, TrustlineitemshowUpdate, TrustlineitemshowDb
from clio_client.models.trust_line_item_show import TrustLineItemShow

def convert_sdk_to_trustlineitemshowout(src: TrustLineItemShow) -> TrustlineitemshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return TrustlineitemshowOut(**src.model_dump())

def convert_trustlineitemshowin_to_sdk(src: TrustlineitemshowIn) -> TrustLineItemShow:
    """Converts a clio_sdk model to clio_client model."""
    return TrustLineItemShow(**src.model_dump())
