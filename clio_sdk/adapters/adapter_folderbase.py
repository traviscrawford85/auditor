# Adapter for folderbase
from clio_sdk.models.folderbase import FolderbaseIn, FolderbaseOut, FolderbaseUpdate, FolderbaseDb
from clio_client.models import folder

def convert_sdk_to_folderbaseout(src: folder) -> FolderbaseOut:
    return FolderbaseOut(**src.dict())

def convert_folderbasein_to_sdk(src: FolderbaseIn) -> folder:
    return folder(**src.dict())
