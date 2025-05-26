# Adapter for mattercontactsbase
from clio_sdk.models.mattercontactsbase import MattercontactsbaseIn, MattercontactsbaseOut, MattercontactsbaseUpdate, MattercontactsbaseDb
from clio_client.models import matter_contacts

def convert_sdk_to_mattercontactsbaseout(src: matter_contacts) -> MattercontactsbaseOut:
    return MattercontactsbaseOut(**src.dict())

def convert_mattercontactsbasein_to_sdk(src: MattercontactsbaseIn) -> matter_contacts:
    return matter_contacts(**src.dict())
