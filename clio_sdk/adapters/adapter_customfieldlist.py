# Adapter for customfieldlist
from clio_sdk.models.customfieldlist import CustomfieldlistIn, CustomfieldlistOut, CustomfieldlistUpdate, CustomfieldlistDb
from clio_client.models.custom_field_list import CustomFieldList

def convert_sdk_to_customfieldlistout(src: CustomFieldList) -> CustomfieldlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return CustomfieldlistOut(**src.model_dump())

def convert_customfieldlistin_to_sdk(src: CustomfieldlistIn) -> CustomFieldList:
    """Converts a clio_sdk model to clio_client model."""
    return CustomFieldList(**src.model_dump())
