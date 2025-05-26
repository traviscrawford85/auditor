# Adapter for communicationbase
from clio_sdk.models.communicationbase import CommunicationBaseIn, CommunicationbaseOut, CommunicationbaseUpdate, CommunicationbaseDb
from clio_client.models.communication import Communication

def convert_sdk_to_communicationbaseout(src: Communication) -> CommunicationbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return CommunicationbaseOut(**src.model_dump())

def convert_communicationbasein_to_sdk(src: CommunicationBaseIn) -> Communication:
    """Converts a clio_sdk model to clio_client model."""
    return Communication(**src.model_dump())
