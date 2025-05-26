# Adapter for allocationbase
from clio_sdk.models.allocationbase import AllocationbaseIn, AllocationbaseOut, AllocationbaseUpdate, AllocationbaseDb
from clio_client.models import allocation

def convert_sdk_to_allocationbaseout(src: allocation) -> AllocationbaseOut:
    return AllocationbaseOut(**src.dict())

def convert_allocationbasein_to_sdk(src: AllocationbaseIn) -> allocation:
    return allocation(**src.dict())
