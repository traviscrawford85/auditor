# Adapter for picklistoptionbase
from clio_sdk.models.picklistoptionbase import PicklistoptionBaseIn, PicklistoptionbaseOut, PicklistoptionbaseUpdate, PicklistoptionbaseDb
from clio_client.models.picklist_option import PicklistOption

def convert_sdk_to_picklistoptionbaseout(src: PicklistOption) -> PicklistoptionbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return PicklistoptionbaseOut(**src.model_dump())

def convert_picklistoptionbasein_to_sdk(src: PicklistoptionBaseIn) -> PicklistOption:
    """Converts a clio_sdk model to clio_client model."""
    return PicklistOption(**src.model_dump())
