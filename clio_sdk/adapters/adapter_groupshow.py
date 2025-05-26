# Adapter for groupshow
from clio_sdk.models.groupshow import GroupshowIn, GroupshowOut, GroupshowUpdate, GroupshowDb
from clio_client.models import group_show

def convert_sdk_to_groupshowout(src: group_show) -> GroupshowOut:
    return GroupshowOut(**src.dict())

def convert_groupshowin_to_sdk(src: GroupshowIn) -> group_show:
    return group_show(**src.dict())
