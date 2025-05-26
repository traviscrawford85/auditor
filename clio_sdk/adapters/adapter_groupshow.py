# Adapter for groupshow
from clio_sdk.models.groupshow import GroupshowIn, GroupshowOut, GroupshowUpdate, GroupshowDb
from clio_client.models.group_show import GroupShow

def convert_sdk_to_groupshowout(src: GroupShow) -> GroupshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return GroupshowOut(**src.model_dump())

def convert_groupshowin_to_sdk(src: GroupshowIn) -> GroupShow:
    """Converts a clio_sdk model to clio_client model."""
    return GroupShow(**src.model_dump())
