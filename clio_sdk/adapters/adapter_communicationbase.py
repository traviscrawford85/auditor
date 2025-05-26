# Adapter for communicationbase
from clio_sdk.models.communicationbase import CommunicationbaseIn, CommunicationbaseOut, CommunicationbaseUpdate, CommunicationbaseDb
from clio_client.models import communication

def convert_sdk_to_communicationbaseout(src: communication) -> CommunicationbaseOut:
    return CommunicationbaseOut(**src.dict())

def convert_communicationbasein_to_sdk(src: CommunicationbaseIn) -> communication:
    return communication(**src.dict())
