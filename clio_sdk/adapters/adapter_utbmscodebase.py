# Adapter for utbmscodebase
from clio_sdk.models.utbmscodebase import UtbmscodeBaseIn, UtbmscodebaseOut, UtbmscodebaseUpdate, UtbmscodebaseDb
from clio_client.models.utbms_code import UtbmsCode

def convert_sdk_to_utbmscodebaseout(src: UtbmsCode) -> UtbmscodebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return UtbmscodebaseOut(**src.model_dump())

def convert_utbmscodebasein_to_sdk(src: UtbmscodeBaseIn) -> UtbmsCode:
    """Converts a clio_sdk model to clio_client model."""
    return UtbmsCode(**src.model_dump())
