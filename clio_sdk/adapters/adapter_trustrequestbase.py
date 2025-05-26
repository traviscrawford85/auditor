# Adapter for trustrequestbase
from clio_sdk.models.trustrequestbase import TrustrequestBaseIn, TrustrequestbaseOut, TrustrequestbaseUpdate, TrustrequestbaseDb
from clio_client.models.trust_request import TrustRequest

def convert_sdk_to_trustrequestbaseout(src: TrustRequest) -> TrustrequestbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return TrustrequestbaseOut(**src.model_dump())

def convert_trustrequestbasein_to_sdk(src: TrustrequestBaseIn) -> TrustRequest:
    """Converts a clio_sdk model to clio_client model."""
    return TrustRequest(**src.model_dump())
