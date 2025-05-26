# Adapter for legalaidukbillbase
from clio_sdk.models.legalaidukbillbase import LegalaidukbillbaseIn, LegalaidukbillbaseOut, LegalaidukbillbaseUpdate, LegalaidukbillbaseDb
from clio_client.models import legal_aid_uk_bill_base

def convert_sdk_to_legalaidukbillbaseout(src: legal_aid_uk_bill_base) -> LegalaidukbillbaseOut:
    return LegalaidukbillbaseOut(**src.dict())

def convert_legalaidukbillbasein_to_sdk(src: LegalaidukbillbaseIn) -> legal_aid_uk_bill_base:
    return legal_aid_uk_bill_base(**src.dict())
