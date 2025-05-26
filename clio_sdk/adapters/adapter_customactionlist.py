# Adapter for customactionlist
from clio_sdk.models.customactionlist import CustomactionlistIn, CustomactionlistOut, CustomactionlistUpdate, CustomactionlistDb
from clio_client.models.custom_action_list import CustomActionList

def convert_sdk_to_customactionlistout(src: CustomActionList) -> CustomactionlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return CustomactionlistOut(**src.model_dump())

def convert_customactionlistin_to_sdk(src: CustomactionlistIn) -> CustomActionList:
    """Converts a clio_sdk model to clio_client model."""
    return CustomActionList(**src.model_dump())
