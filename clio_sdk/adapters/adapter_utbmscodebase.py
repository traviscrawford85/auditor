# Adapter for utbmscodebase
from clio_sdk.models.utbmscodebase import UtbmscodebaseIn, UtbmscodebaseOut, UtbmscodebaseUpdate, UtbmscodebaseDb
from clio_client.models import utbms_code

def convert_sdk_to_utbmscodebaseout(src: utbms_code) -> UtbmscodebaseOut:
    return UtbmscodebaseOut(**src.dict())

def convert_utbmscodebasein_to_sdk(src: UtbmscodebaseIn) -> utbms_code:
    return utbms_code(**src.dict())
