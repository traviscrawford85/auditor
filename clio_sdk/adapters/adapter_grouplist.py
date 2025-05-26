# Adapter for grouplist
from clio_sdk.models.grouplist import GrouplistIn, GrouplistOut, GrouplistUpdate, GrouplistDb
from clio_client.models import group_list

def convert_sdk_to_grouplistout(src: group_list) -> GrouplistOut:
    return GrouplistOut(**src.dict())

def convert_grouplistin_to_sdk(src: GrouplistIn) -> group_list:
    return group_list(**src.dict())
