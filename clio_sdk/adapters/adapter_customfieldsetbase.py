# Adapter for customfieldsetbase
from clio_sdk.models.customfieldsetbase import CustomfieldsetBaseIn, CustomfieldsetbaseOut, CustomfieldsetbaseUpdate, CustomfieldsetbaseDb
from clio_client.models.custom_field_set import CustomFieldSet

def convert_sdk_to_customfieldsetbaseout(src: CustomFieldSet) -> CustomfieldsetbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return CustomfieldsetbaseOut(**src.model_dump())

def convert_customfieldsetbasein_to_sdk(src: CustomfieldsetBaseIn) -> CustomFieldSet:
    """Converts a clio_sdk model to clio_client model."""
    return CustomFieldSet(**src.model_dump())
