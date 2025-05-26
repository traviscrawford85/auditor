# Adapter for grouplist
from clio_sdk.models.grouplist import GrouplistIn, GrouplistOut, GrouplistUpdate, GrouplistDb
from clio_client.models.group_list import GroupList

def convert_sdk_to_grouplistout(src: GroupList) -> GrouplistOut:
    """Converts a clio_client model to clio_sdk model."""
    return GrouplistOut(**src.model_dump())

def convert_grouplistin_to_sdk(src: GrouplistIn) -> GroupList:
    """Converts a clio_sdk model to clio_client model."""
    return GroupList(**src.model_dump())
