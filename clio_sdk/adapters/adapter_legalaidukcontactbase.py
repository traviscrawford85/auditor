# Adapter for legalaidukcontactbase
from clio_sdk.models.legalaidukcontactbase import LegalaidukcontactbaseIn, LegalaidukcontactbaseOut, LegalaidukcontactbaseUpdate, LegalaidukcontactbaseDb
from clio_client.models import legal_aid_uk_contact_base

def convert_sdk_to_legalaidukcontactbaseout(src: legal_aid_uk_contact_base) -> LegalaidukcontactbaseOut:
    return LegalaidukcontactbaseOut(**src.dict())

def convert_legalaidukcontactbasein_to_sdk(src: LegalaidukcontactbaseIn) -> legal_aid_uk_contact_base:
    return legal_aid_uk_contact_base(**src.dict())
