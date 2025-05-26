# Adapter for customactionbase
from clio_sdk.models.customactionbase import CustomactionBaseIn, CustomactionbaseOut, CustomactionbaseUpdate, CustomactionbaseDb
from clio_client.models.custom_action import CustomAction

def convert_sdk_to_customactionbaseout(src: CustomAction) -> CustomactionbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return CustomactionbaseOut(**src.model_dump())

def convert_customactionbasein_to_sdk(src: CustomactionBaseIn) -> CustomAction:
    """Converts a clio_sdk model to clio_client model."""
    return CustomAction(**src.model_dump())
