# Adapter for matterbase
from clio_sdk.models.matterbase import MatterbaseIn, MatterbaseOut, MatterbaseUpdate, MatterbaseDb
from clio_client.models import matter

def convert_sdk_to_matterbaseout(src: matter) -> MatterbaseOut:
    return MatterbaseOut(**src.dict())

def convert_matterbasein_to_sdk(src: MatterbaseIn) -> matter:
    return matter(**src.dict())
