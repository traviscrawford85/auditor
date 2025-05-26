# Adapter for communicationlist
from clio_sdk.models.communicationlist import CommunicationlistIn, CommunicationlistOut, CommunicationlistUpdate, CommunicationlistDb
from clio_client.models import communication_list

def convert_sdk_to_communicationlistout(src: communication_list) -> CommunicationlistOut:
    return CommunicationlistOut(**src.dict())

def convert_communicationlistin_to_sdk(src: CommunicationlistIn) -> communication_list:
    return communication_list(**src.dict())
