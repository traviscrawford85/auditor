# Adapter for customfieldvaluebase
from clio_sdk.models.customfieldvaluebase import CustomfieldvalueBaseIn, CustomfieldvaluebaseOut, CustomfieldvaluebaseUpdate, CustomfieldvaluebaseDb
from clio_client.models.custom_field_value import CustomFieldValue

def convert_sdk_to_customfieldvaluebaseout(src: CustomFieldValue) -> CustomfieldvaluebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return CustomfieldvaluebaseOut(**src.model_dump())

def convert_customfieldvaluebasein_to_sdk(src: CustomfieldvalueBaseIn) -> CustomFieldValue:
    """Converts a clio_sdk model to clio_client model."""
    return CustomFieldValue(**src.model_dump())
