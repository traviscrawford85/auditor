# Adapter for trustrequestshow
from clio_sdk.models.trustrequestshow import TrustrequestshowIn, TrustrequestshowOut, TrustrequestshowUpdate, TrustrequestshowDb
from clio_client.models import trust_request_show

def convert_sdk_to_trustrequestshowout(src: trust_request_show) -> TrustrequestshowOut:
    return TrustrequestshowOut(**src.dict())

def convert_trustrequestshowin_to_sdk(src: TrustrequestshowIn) -> trust_request_show:
    return trust_request_show(**src.dict())
