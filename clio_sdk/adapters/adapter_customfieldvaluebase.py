# Adapter for customfieldvaluebase
from clio_sdk.models.customfieldvaluebase import CustomfieldvaluebaseIn, CustomfieldvaluebaseOut, CustomfieldvaluebaseUpdate, CustomfieldvaluebaseDb
from clio_client.models import custom_field_value

def convert_sdk_to_customfieldvaluebaseout(src: custom_field_value) -> CustomfieldvaluebaseOut:
    return CustomfieldvaluebaseOut(**src.dict())

def convert_customfieldvaluebasein_to_sdk(src: CustomfieldvaluebaseIn) -> custom_field_value:
    return custom_field_value(**src.dict())
