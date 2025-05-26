# Adapter for utbmscodelist
from clio_sdk.models.utbmscodelist import UtbmscodelistIn, UtbmscodelistOut, UtbmscodelistUpdate, UtbmscodelistDb
from clio_client.models import utbms_code_list

def convert_sdk_to_utbmscodelistout(src: utbms_code_list) -> UtbmscodelistOut:
    return UtbmscodelistOut(**src.dict())

def convert_utbmscodelistin_to_sdk(src: UtbmscodelistIn) -> utbms_code_list:
    return utbms_code_list(**src.dict())
