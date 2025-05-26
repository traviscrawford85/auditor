# Adapter for legalaidukcontactbase
from clio_sdk.models.legalaidukcontactbase import LegalaidukcontactBaseIn, LegalaidukcontactbaseOut, LegalaidukcontactbaseUpdate, LegalaidukcontactbaseDb
from clio_client.models.legal_aid_uk_contact_base import LegalAidUkContactBase

def convert_sdk_to_legalaidukcontactbaseout(src: LegalAidUkContactBase) -> LegalaidukcontactbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return LegalaidukcontactbaseOut(**src.model_dump())

def convert_legalaidukcontactbasein_to_sdk(src: LegalaidukcontactBaseIn) -> LegalAidUkContactBase:
    """Converts a clio_sdk model to clio_client model."""
    return LegalAidUkContactBase(**src.model_dump())
