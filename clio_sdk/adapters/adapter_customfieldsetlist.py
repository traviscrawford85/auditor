# Adapter for customfieldsetlist
from clio_sdk.models.customfieldsetlist import CustomfieldsetlistIn, CustomfieldsetlistOut, CustomfieldsetlistUpdate, CustomfieldsetlistDb
from clio_client.models.custom_field_set_list import CustomFieldSetList

def convert_sdk_to_customfieldsetlistout(src: CustomFieldSetList) -> CustomfieldsetlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return CustomfieldsetlistOut(**src.model_dump())

def convert_customfieldsetlistin_to_sdk(src: CustomfieldsetlistIn) -> CustomFieldSetList:
    """Converts a clio_sdk model to clio_client model."""
    return CustomFieldSetList(**src.model_dump())
