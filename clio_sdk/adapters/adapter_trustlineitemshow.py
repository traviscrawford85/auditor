# Adapter for trustlineitemshow
from clio_sdk.models.trustlineitemshow import TrustlineitemshowIn, TrustlineitemshowOut, TrustlineitemshowUpdate, TrustlineitemshowDb
from clio_client.models import trust_line_item_show

def convert_sdk_to_trustlineitemshowout(src: trust_line_item_show) -> TrustlineitemshowOut:
    return TrustlineitemshowOut(**src.dict())

def convert_trustlineitemshowin_to_sdk(src: TrustlineitemshowIn) -> trust_line_item_show:
    return trust_line_item_show(**src.dict())
