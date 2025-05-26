# Adapter for folderlist
from clio_sdk.models.folderlist import FolderlistIn, FolderlistOut, FolderlistUpdate, FolderlistDb
from clio_client.models.folder_list import FolderList

def convert_sdk_to_folderlistout(src: FolderList) -> FolderlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return FolderlistOut(**src.model_dump())

def convert_folderlistin_to_sdk(src: FolderlistIn) -> FolderList:
    """Converts a clio_sdk model to clio_client model."""
    return FolderList(**src.model_dump())
