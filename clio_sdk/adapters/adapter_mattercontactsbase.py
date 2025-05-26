# Adapter for mattercontactsbase
from clio_sdk.models.mattercontactsbase import MattercontactsBaseIn, MattercontactsbaseOut, MattercontactsbaseUpdate, MattercontactsbaseDb
from clio_client.models.matter_contacts import MatterContacts

def convert_sdk_to_mattercontactsbaseout(src: MatterContacts) -> MattercontactsbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return MattercontactsbaseOut(**src.model_dump())

def convert_mattercontactsbasein_to_sdk(src: MattercontactsBaseIn) -> MatterContacts:
    """Converts a clio_sdk model to clio_client model."""
    return MatterContacts(**src.model_dump())
