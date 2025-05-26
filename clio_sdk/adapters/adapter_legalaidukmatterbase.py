# Adapter for legalaidukmatterbase
from clio_sdk.models.legalaidukmatterbase import LegalaidukmatterBaseIn, LegalaidukmatterbaseOut, LegalaidukmatterbaseUpdate, LegalaidukmatterbaseDb
from clio_client.models.legal_aid_uk_matter_base import LegalAidUkMatterBase

def convert_sdk_to_legalaidukmatterbaseout(src: LegalAidUkMatterBase) -> LegalaidukmatterbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return LegalaidukmatterbaseOut(**src.model_dump())

def convert_legalaidukmatterbasein_to_sdk(src: LegalaidukmatterBaseIn) -> LegalAidUkMatterBase:
    """Converts a clio_sdk model to clio_client model."""
    return LegalAidUkMatterBase(**src.model_dump())
