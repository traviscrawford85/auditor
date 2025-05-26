# Adapter for mattercontactslist
from clio_sdk.models.mattercontactslist import MattercontactslistIn, MattercontactslistOut, MattercontactslistUpdate, MattercontactslistDb
from clio_client.models import matter_contacts_list

def convert_sdk_to_mattercontactslistout(src: matter_contacts_list) -> MattercontactslistOut:
    return MattercontactslistOut(**src.dict())

def convert_mattercontactslistin_to_sdk(src: MattercontactslistIn) -> matter_contacts_list:
    return matter_contacts_list(**src.dict())
