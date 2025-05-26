# Adapter for linkedfolderbase
from clio_sdk.models.linkedfolderbase import LinkedfolderBaseIn, LinkedfolderbaseOut, LinkedfolderbaseUpdate, LinkedfolderbaseDb
from clio_client.models.linked_folder_base import LinkedFolderBase

def convert_sdk_to_linkedfolderbaseout(src: LinkedFolderBase) -> LinkedfolderbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return LinkedfolderbaseOut(**src.model_dump())

def convert_linkedfolderbasein_to_sdk(src: LinkedfolderBaseIn) -> LinkedFolderBase:
    """Converts a clio_sdk model to clio_client model."""
    return LinkedFolderBase(**src.model_dump())
