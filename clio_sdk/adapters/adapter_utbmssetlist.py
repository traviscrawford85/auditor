# Adapter for utbmssetlist
from clio_sdk.models.utbmssetlist import UtbmssetlistIn, UtbmssetlistOut, UtbmssetlistUpdate, UtbmssetlistDb
from clio_client.models import utbms_set_list

def convert_sdk_to_utbmssetlistout(src: utbms_set_list) -> UtbmssetlistOut:
    return UtbmssetlistOut(**src.dict())

def convert_utbmssetlistin_to_sdk(src: UtbmssetlistIn) -> utbms_set_list:
    return utbms_set_list(**src.dict())
