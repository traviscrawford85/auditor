# Adapter for legalaidukbillbase
from clio_sdk.models.legalaidukbillbase import LegalaidukbillBaseIn, LegalaidukbillbaseOut, LegalaidukbillbaseUpdate, LegalaidukbillbaseDb
from clio_client.models.legal_aid_uk_bill_base import LegalAidUkBillBase

def convert_sdk_to_legalaidukbillbaseout(src: LegalAidUkBillBase) -> LegalaidukbillbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return LegalaidukbillbaseOut(**src.model_dump())

def convert_legalaidukbillbasein_to_sdk(src: LegalaidukbillBaseIn) -> LegalAidUkBillBase:
    """Converts a clio_sdk model to clio_client model."""
    return LegalAidUkBillBase(**src.model_dump())
