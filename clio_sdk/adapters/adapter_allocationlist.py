# Adapter for allocationlist
from clio_sdk.models.allocationlist import AllocationlistIn, AllocationlistOut, AllocationlistUpdate, AllocationlistDb
from clio_client.models.allocation_list import AllocationList

def convert_sdk_to_allocationlistout(src: AllocationList) -> AllocationlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return AllocationlistOut(**src.model_dump())

def convert_allocationlistin_to_sdk(src: AllocationlistIn) -> AllocationList:
    """Converts a clio_sdk model to clio_client model."""
    return AllocationList(**src.model_dump())
