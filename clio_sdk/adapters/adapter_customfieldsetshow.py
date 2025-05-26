# Adapter for customfieldsetshow
from clio_sdk.models.customfieldsetshow import CustomfieldsetshowIn, CustomfieldsetshowOut, CustomfieldsetshowUpdate, CustomfieldsetshowDb
from clio_client.models import custom_field_set_show

def convert_sdk_to_customfieldsetshowout(src: custom_field_set_show) -> CustomfieldsetshowOut:
    return CustomfieldsetshowOut(**src.dict())

def convert_customfieldsetshowin_to_sdk(src: CustomfieldsetshowIn) -> custom_field_set_show:
    return custom_field_set_show(**src.dict())
