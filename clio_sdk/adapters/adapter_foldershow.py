# Adapter for foldershow
from clio_sdk.models.foldershow import FoldershowIn, FoldershowOut, FoldershowUpdate, FoldershowDb
from clio_client.models import folder_show

def convert_sdk_to_foldershowout(src: folder_show) -> FoldershowOut:
    return FoldershowOut(**src.dict())

def convert_foldershowin_to_sdk(src: FoldershowIn) -> folder_show:
    return folder_show(**src.dict())
