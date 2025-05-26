# Adapter for customactionlist
from clio_sdk.models.customactionlist import CustomactionlistIn, CustomactionlistOut, CustomactionlistUpdate, CustomactionlistDb
from clio_client.models import custom_action_list

def convert_sdk_to_customactionlistout(src: custom_action_list) -> CustomactionlistOut:
    return CustomactionlistOut(**src.dict())

def convert_customactionlistin_to_sdk(src: CustomactionlistIn) -> custom_action_list:
    return custom_action_list(**src.dict())
