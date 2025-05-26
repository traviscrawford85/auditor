# Adapter for customactionshow
from clio_sdk.models.customactionshow import CustomactionshowIn, CustomactionshowOut, CustomactionshowUpdate, CustomactionshowDb
from clio_client.models import custom_action_show

def convert_sdk_to_customactionshowout(src: custom_action_show) -> CustomactionshowOut:
    return CustomactionshowOut(**src.dict())

def convert_customactionshowin_to_sdk(src: CustomactionshowIn) -> custom_action_show:
    return custom_action_show(**src.dict())
