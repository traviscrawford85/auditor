# Adapter for customfieldsetbase
from clio_sdk.models.customfieldsetbase import CustomfieldsetbaseIn, CustomfieldsetbaseOut, CustomfieldsetbaseUpdate, CustomfieldsetbaseDb
from clio_client.models import custom_field_set

def convert_sdk_to_customfieldsetbaseout(src: custom_field_set) -> CustomfieldsetbaseOut:
    return CustomfieldsetbaseOut(**src.dict())

def convert_customfieldsetbasein_to_sdk(src: CustomfieldsetbaseIn) -> custom_field_set:
    return custom_field_set(**src.dict())
