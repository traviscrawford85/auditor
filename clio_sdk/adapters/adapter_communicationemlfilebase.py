# Adapter for communicationemlfilebase
from clio_sdk.models.communicationemlfilebase import CommunicationemlfilebaseIn, CommunicationemlfilebaseOut, CommunicationemlfilebaseUpdate, CommunicationemlfilebaseDb
from clio_client.models import communication_eml_file_base

def convert_sdk_to_communicationemlfilebaseout(src: communication_eml_file_base) -> CommunicationemlfilebaseOut:
    return CommunicationemlfilebaseOut(**src.dict())

def convert_communicationemlfilebasein_to_sdk(src: CommunicationemlfilebaseIn) -> communication_eml_file_base:
    return communication_eml_file_base(**src.dict())
