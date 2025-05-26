# Adapter for utbmssetbase
from clio_sdk.models.utbmssetbase import UtbmssetbaseIn, UtbmssetbaseOut, UtbmssetbaseUpdate, UtbmssetbaseDb
from clio_client.models import utbms_set

def convert_sdk_to_utbmssetbaseout(src: utbms_set) -> UtbmssetbaseOut:
    return UtbmssetbaseOut(**src.dict())

def convert_utbmssetbasein_to_sdk(src: UtbmssetbaseIn) -> utbms_set:
    return utbms_set(**src.dict())
