# Adapter for groupbase
from clio_sdk.models.groupbase import GroupbaseIn, GroupbaseOut, GroupbaseUpdate, GroupbaseDb
from clio_client.models import group

def convert_sdk_to_groupbaseout(src: group) -> GroupbaseOut:
    return GroupbaseOut(**src.dict())

def convert_groupbasein_to_sdk(src: GroupbaseIn) -> group:
    return group(**src.dict())
