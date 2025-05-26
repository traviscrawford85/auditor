# Adapter for customfieldsetshow
from clio_sdk.models.customfieldsetshow import CustomfieldsetshowIn, CustomfieldsetshowOut, CustomfieldsetshowUpdate, CustomfieldsetshowDb
from clio_client.models.custom_field_set_show import CustomFieldSetShow

def convert_sdk_to_customfieldsetshowout(src: CustomFieldSetShow) -> CustomfieldsetshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return CustomfieldsetshowOut(**src.model_dump())

def convert_customfieldsetshowin_to_sdk(src: CustomfieldsetshowIn) -> CustomFieldSetShow:
    """Converts a clio_sdk model to clio_client model."""
    return CustomFieldSetShow(**src.model_dump())
