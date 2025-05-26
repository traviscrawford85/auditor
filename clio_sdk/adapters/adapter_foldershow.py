# Adapter for foldershow
from clio_sdk.models.foldershow import FoldershowIn, FoldershowOut, FoldershowUpdate, FoldershowDb
from clio_client.models.folder_show import FolderShow

def convert_sdk_to_foldershowout(src: FolderShow) -> FoldershowOut:
    """Converts a clio_client model to clio_sdk model."""
    return FoldershowOut(**src.model_dump())

def convert_foldershowin_to_sdk(src: FoldershowIn) -> FolderShow:
    """Converts a clio_sdk model to clio_client model."""
    return FolderShow(**src.model_dump())
