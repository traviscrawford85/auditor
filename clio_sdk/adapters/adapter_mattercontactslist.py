# Adapter for mattercontactslist
from clio_sdk.models.mattercontactslist import MattercontactslistIn, MattercontactslistOut, MattercontactslistUpdate, MattercontactslistDb
from clio_client.models.matter_contacts_list import MatterContactsList

def convert_sdk_to_mattercontactslistout(src: MatterContactsList) -> MattercontactslistOut:
    """Converts a clio_client model to clio_sdk model."""
    return MattercontactslistOut(**src.model_dump())

def convert_mattercontactslistin_to_sdk(src: MattercontactslistIn) -> MatterContactsList:
    """Converts a clio_sdk model to clio_client model."""
    return MatterContactsList(**src.model_dump())
