# Adapter for utbmscodeshow
from clio_sdk.models.utbmscodeshow import UtbmscodeshowIn, UtbmscodeshowOut, UtbmscodeshowUpdate, UtbmscodeshowDb
from clio_client.models.utbms_code_show import UtbmsCodeShow

def convert_sdk_to_utbmscodeshowout(src: UtbmsCodeShow) -> UtbmscodeshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return UtbmscodeshowOut(**src.model_dump())

def convert_utbmscodeshowin_to_sdk(src: UtbmscodeshowIn) -> UtbmsCodeShow:
    """Converts a clio_sdk model to clio_client model."""
    return UtbmsCodeShow(**src.model_dump())
