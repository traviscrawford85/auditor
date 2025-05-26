# Adapter for evergreenretainerbase
from clio_sdk.models.evergreenretainerbase import EvergreenretainerbaseIn, EvergreenretainerbaseOut, EvergreenretainerbaseUpdate, EvergreenretainerbaseDb
from clio_client.models import evergreen_retainer_base

def convert_sdk_to_evergreenretainerbaseout(src: evergreen_retainer_base) -> EvergreenretainerbaseOut:
    return EvergreenretainerbaseOut(**src.dict())

def convert_evergreenretainerbasein_to_sdk(src: EvergreenretainerbaseIn) -> evergreen_retainer_base:
    return evergreen_retainer_base(**src.dict())
