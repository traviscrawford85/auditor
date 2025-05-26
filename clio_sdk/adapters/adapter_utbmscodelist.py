# Adapter for utbmscodelist
from clio_sdk.models.utbmscodelist import UtbmscodelistIn, UtbmscodelistOut, UtbmscodelistUpdate, UtbmscodelistDb
from clio_client.models.utbms_code_list import UtbmsCodeList

def convert_sdk_to_utbmscodelistout(src: UtbmsCodeList) -> UtbmscodelistOut:
    """Converts a clio_client model to clio_sdk model."""
    return UtbmscodelistOut(**src.model_dump())

def convert_utbmscodelistin_to_sdk(src: UtbmscodelistIn) -> UtbmsCodeList:
    """Converts a clio_sdk model to clio_client model."""
    return UtbmsCodeList(**src.model_dump())
