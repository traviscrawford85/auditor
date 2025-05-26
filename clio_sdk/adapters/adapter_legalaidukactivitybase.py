# Adapter for legalaidukactivitybase
from clio_sdk.models.legalaidukactivitybase import LegalaidukactivitybaseIn, LegalaidukactivitybaseOut, LegalaidukactivitybaseUpdate, LegalaidukactivitybaseDb
from clio_client.models import legal_aid_uk_activity_base

def convert_sdk_to_legalaidukactivitybaseout(src: legal_aid_uk_activity_base) -> LegalaidukactivitybaseOut:
    return LegalaidukactivitybaseOut(**src.dict())

def convert_legalaidukactivitybasein_to_sdk(src: LegalaidukactivitybaseIn) -> legal_aid_uk_activity_base:
    return legal_aid_uk_activity_base(**src.dict())
