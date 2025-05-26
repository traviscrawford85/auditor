# Adapter for folderbase
from clio_sdk.models.folderbase import FolderBaseIn, FolderbaseOut, FolderbaseUpdate, FolderbaseDb
from clio_client.models.folder import Folder

def convert_sdk_to_folderbaseout(src: Folder) -> FolderbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return FolderbaseOut(**src.model_dump())

def convert_folderbasein_to_sdk(src: FolderBaseIn) -> Folder:
    """Converts a clio_sdk model to clio_client model."""
    return Folder(**src.model_dump())
