# Adapter for legalaidukmatterbase
from clio_sdk.models.legalaidukmatterbase import LegalaidukmatterbaseIn, LegalaidukmatterbaseOut, LegalaidukmatterbaseUpdate, LegalaidukmatterbaseDb
from clio_client.models import legal_aid_uk_matter_base

def convert_sdk_to_legalaidukmatterbaseout(src: legal_aid_uk_matter_base) -> LegalaidukmatterbaseOut:
    return LegalaidukmatterbaseOut(**src.dict())

def convert_legalaidukmatterbasein_to_sdk(src: LegalaidukmatterbaseIn) -> legal_aid_uk_matter_base:
    return legal_aid_uk_matter_base(**src.dict())
