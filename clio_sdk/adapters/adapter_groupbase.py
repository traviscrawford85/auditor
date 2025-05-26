# Adapter for groupbase
from clio_sdk.models.groupbase import GroupBaseIn, GroupbaseOut, GroupbaseUpdate, GroupbaseDb
from clio_client.models.group import Group

def convert_sdk_to_groupbaseout(src: Group) -> GroupbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return GroupbaseOut(**src.model_dump())

def convert_groupbasein_to_sdk(src: GroupBaseIn) -> Group:
    """Converts a clio_sdk model to clio_client model."""
    return Group(**src.model_dump())
