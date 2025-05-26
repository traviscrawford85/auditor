# Adapter for folderlist
from clio_sdk.models.folderlist import FolderlistIn, FolderlistOut, FolderlistUpdate, FolderlistDb
from clio_client.models import folder_list

def convert_sdk_to_folderlistout(src: folder_list) -> FolderlistOut:
    return FolderlistOut(**src.dict())

def convert_folderlistin_to_sdk(src: FolderlistIn) -> folder_list:
    return folder_list(**src.dict())
