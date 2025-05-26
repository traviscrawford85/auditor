# Adapter for communicationshow
from clio_sdk.models.communicationshow import CommunicationshowIn, CommunicationshowOut, CommunicationshowUpdate, CommunicationshowDb
from clio_client.models import communication_show

def convert_sdk_to_communicationshowout(src: communication_show) -> CommunicationshowOut:
    return CommunicationshowOut(**src.dict())

def convert_communicationshowin_to_sdk(src: CommunicationshowIn) -> communication_show:
    return communication_show(**src.dict())
