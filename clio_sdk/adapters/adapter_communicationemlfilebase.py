# Adapter for communicationemlfilebase
from clio_sdk.models.communicationemlfilebase import CommunicationemlfileBaseIn, CommunicationemlfilebaseOut, CommunicationemlfilebaseUpdate, CommunicationemlfilebaseDb
from clio_client.models.communication_eml_file_base import CommunicationEmlFileBase

def convert_sdk_to_communicationemlfilebaseout(src: CommunicationEmlFileBase) -> CommunicationemlfilebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return CommunicationemlfilebaseOut(**src.model_dump())

def convert_communicationemlfilebasein_to_sdk(src: CommunicationemlfileBaseIn) -> CommunicationEmlFileBase:
    """Converts a clio_sdk model to clio_client model."""
    return CommunicationEmlFileBase(**src.model_dump())
