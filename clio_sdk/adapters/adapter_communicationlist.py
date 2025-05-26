# Adapter for communicationlist
from clio_sdk.models.communicationlist import CommunicationlistIn, CommunicationlistOut, CommunicationlistUpdate, CommunicationlistDb
from clio_client.models.communication_list import CommunicationList

def convert_sdk_to_communicationlistout(src: CommunicationList) -> CommunicationlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return CommunicationlistOut(**src.model_dump())

def convert_communicationlistin_to_sdk(src: CommunicationlistIn) -> CommunicationList:
    """Converts a clio_sdk model to clio_client model."""
    return CommunicationList(**src.model_dump())
