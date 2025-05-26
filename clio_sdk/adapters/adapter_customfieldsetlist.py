# Adapter for customfieldsetlist
from clio_sdk.models.customfieldsetlist import CustomfieldsetlistIn, CustomfieldsetlistOut, CustomfieldsetlistUpdate, CustomfieldsetlistDb
from clio_client.models import custom_field_set_list

def convert_sdk_to_customfieldsetlistout(src: custom_field_set_list) -> CustomfieldsetlistOut:
    return CustomfieldsetlistOut(**src.dict())

def convert_customfieldsetlistin_to_sdk(src: CustomfieldsetlistIn) -> custom_field_set_list:
    return custom_field_set_list(**src.dict())
