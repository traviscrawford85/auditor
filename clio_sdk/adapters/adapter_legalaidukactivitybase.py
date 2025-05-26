# Adapter for legalaidukactivitybase
from clio_sdk.models.legalaidukactivitybase import LegalaidukactivityBaseIn, LegalaidukactivitybaseOut, LegalaidukactivitybaseUpdate, LegalaidukactivitybaseDb
from clio_client.models.legal_aid_uk_activity_base import LegalAidUkActivityBase

def convert_sdk_to_legalaidukactivitybaseout(src: LegalAidUkActivityBase) -> LegalaidukactivitybaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return LegalaidukactivitybaseOut(**src.model_dump())

def convert_legalaidukactivitybasein_to_sdk(src: LegalaidukactivityBaseIn) -> LegalAidUkActivityBase:
    """Converts a clio_sdk model to clio_client model."""
    return LegalAidUkActivityBase(**src.model_dump())
