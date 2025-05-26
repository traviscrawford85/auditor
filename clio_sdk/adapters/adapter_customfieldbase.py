# Adapter for customfieldbase
from clio_sdk.models.customfieldbase import CustomfieldbaseIn, CustomfieldbaseOut, CustomfieldbaseUpdate, CustomfieldbaseDb
from clio_client.models import custom_field

def convert_sdk_to_customfieldbaseout(src: custom_field) -> CustomfieldbaseOut:
    return CustomfieldbaseOut(**src.dict())

def convert_customfieldbasein_to_sdk(src: CustomfieldbaseIn) -> custom_field:
    return custom_field(**src.dict())
