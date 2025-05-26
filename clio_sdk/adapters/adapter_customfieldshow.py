# Adapter for customfieldshow
from clio_sdk.models.customfieldshow import CustomfieldshowIn, CustomfieldshowOut, CustomfieldshowUpdate, CustomfieldshowDb
from clio_client.models import custom_field_show

def convert_sdk_to_customfieldshowout(src: custom_field_show) -> CustomfieldshowOut:
    return CustomfieldshowOut(**src.dict())

def convert_customfieldshowin_to_sdk(src: CustomfieldshowIn) -> custom_field_show:
    return custom_field_show(**src.dict())
