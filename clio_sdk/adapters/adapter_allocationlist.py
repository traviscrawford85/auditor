# Adapter for allocationlist
from clio_sdk.models.allocationlist import AllocationlistIn, AllocationlistOut, AllocationlistUpdate, AllocationlistDb
from clio_client.models import allocation_list

def convert_sdk_to_allocationlistout(src: allocation_list) -> AllocationlistOut:
    return AllocationlistOut(**src.dict())

def convert_allocationlistin_to_sdk(src: AllocationlistIn) -> allocation_list:
    return allocation_list(**src.dict())
