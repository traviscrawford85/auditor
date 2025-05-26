# Adapter for customactionbase
from clio_sdk.models.customactionbase import CustomactionbaseIn, CustomactionbaseOut, CustomactionbaseUpdate, CustomactionbaseDb
from clio_client.models import custom_action

def convert_sdk_to_customactionbaseout(src: custom_action) -> CustomactionbaseOut:
    return CustomactionbaseOut(**src.dict())

def convert_customactionbasein_to_sdk(src: CustomactionbaseIn) -> custom_action:
    return custom_action(**src.dict())
