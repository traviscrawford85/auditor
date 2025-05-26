# Adapter for customfieldlist
from clio_sdk.models.customfieldlist import CustomfieldlistIn, CustomfieldlistOut, CustomfieldlistUpdate, CustomfieldlistDb
from clio_client.models import custom_field_list

def convert_sdk_to_customfieldlistout(src: custom_field_list) -> CustomfieldlistOut:
    return CustomfieldlistOut(**src.dict())

def convert_customfieldlistin_to_sdk(src: CustomfieldlistIn) -> custom_field_list:
    return custom_field_list(**src.dict())
