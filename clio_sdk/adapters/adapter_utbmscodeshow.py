# Adapter for utbmscodeshow
from clio_sdk.models.utbmscodeshow import UtbmscodeshowIn, UtbmscodeshowOut, UtbmscodeshowUpdate, UtbmscodeshowDb
from clio_client.models import utbms_code_show

def convert_sdk_to_utbmscodeshowout(src: utbms_code_show) -> UtbmscodeshowOut:
    return UtbmscodeshowOut(**src.dict())

def convert_utbmscodeshowin_to_sdk(src: UtbmscodeshowIn) -> utbms_code_show:
    return utbms_code_show(**src.dict())
