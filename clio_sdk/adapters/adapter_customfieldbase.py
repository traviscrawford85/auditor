# Adapter for customfieldbase
from clio_sdk.models.customfieldbase import CustomfieldBaseIn, CustomfieldbaseOut, CustomfieldbaseUpdate, CustomfieldbaseDb
from clio_client.models.custom_field import CustomField

def convert_sdk_to_customfieldbaseout(src: CustomField) -> CustomfieldbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return CustomfieldbaseOut(**src.model_dump())

def convert_customfieldbasein_to_sdk(src: CustomfieldBaseIn) -> CustomField:
    """Converts a clio_sdk model to clio_client model."""
    return CustomField(**src.model_dump())
