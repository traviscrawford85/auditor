# Adapter for picklistoptionbase
from clio_sdk.models.picklistoptionbase import PicklistoptionbaseIn, PicklistoptionbaseOut, PicklistoptionbaseUpdate, PicklistoptionbaseDb
from clio_client.models import picklist_option

def convert_sdk_to_picklistoptionbaseout(src: picklist_option) -> PicklistoptionbaseOut:
    return PicklistoptionbaseOut(**src.dict())

def convert_picklistoptionbasein_to_sdk(src: PicklistoptionbaseIn) -> picklist_option:
    return picklist_option(**src.dict())
