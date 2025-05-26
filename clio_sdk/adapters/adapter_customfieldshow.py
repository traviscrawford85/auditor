# Adapter for customfieldshow
from clio_sdk.models.customfieldshow import CustomfieldshowIn, CustomfieldshowOut, CustomfieldshowUpdate, CustomfieldshowDb
from clio_client.models.custom_field_show import CustomFieldShow

def convert_sdk_to_customfieldshowout(src: CustomFieldShow) -> CustomfieldshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return CustomfieldshowOut(**src.model_dump())

def convert_customfieldshowin_to_sdk(src: CustomfieldshowIn) -> CustomFieldShow:
    """Converts a clio_sdk model to clio_client model."""
    return CustomFieldShow(**src.model_dump())
