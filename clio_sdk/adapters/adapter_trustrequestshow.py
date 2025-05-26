# Adapter for trustrequestshow
from clio_sdk.models.trustrequestshow import TrustrequestshowIn, TrustrequestshowOut, TrustrequestshowUpdate, TrustrequestshowDb
from clio_client.models.trust_request_show import TrustRequestShow

def convert_sdk_to_trustrequestshowout(src: TrustRequestShow) -> TrustrequestshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return TrustrequestshowOut(**src.model_dump())

def convert_trustrequestshowin_to_sdk(src: TrustrequestshowIn) -> TrustRequestShow:
    """Converts a clio_sdk model to clio_client model."""
    return TrustRequestShow(**src.model_dump())
