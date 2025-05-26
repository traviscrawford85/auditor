# Adapter for linkedfolderbase
from clio_sdk.models.linkedfolderbase import LinkedfolderbaseIn, LinkedfolderbaseOut, LinkedfolderbaseUpdate, LinkedfolderbaseDb
from clio_client.models import linked_folder_base

def convert_sdk_to_linkedfolderbaseout(src: linked_folder_base) -> LinkedfolderbaseOut:
    return LinkedfolderbaseOut(**src.dict())

def convert_linkedfolderbasein_to_sdk(src: LinkedfolderbaseIn) -> linked_folder_base:
    return linked_folder_base(**src.dict())
