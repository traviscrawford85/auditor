# Adapter for communicationshow
from clio_sdk.models.communicationshow import CommunicationshowIn, CommunicationshowOut, CommunicationshowUpdate, CommunicationshowDb
from clio_client.models.communication_show import CommunicationShow

def convert_sdk_to_communicationshowout(src: CommunicationShow) -> CommunicationshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return CommunicationshowOut(**src.model_dump())

def convert_communicationshowin_to_sdk(src: CommunicationshowIn) -> CommunicationShow:
    """Converts a clio_sdk model to clio_client model."""
    return CommunicationShow(**src.model_dump())
