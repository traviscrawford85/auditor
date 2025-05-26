# Adapter for allocationbase
from clio_sdk.models.allocationbase import AllocationBaseIn, AllocationbaseOut, AllocationbaseUpdate, AllocationbaseDb
from clio_client.models.allocation import Allocation

def convert_sdk_to_allocationbaseout(src: Allocation) -> AllocationbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return AllocationbaseOut(**src.model_dump())

def convert_allocationbasein_to_sdk(src: AllocationBaseIn) -> Allocation:
    """Converts a clio_sdk model to clio_client model."""
    return Allocation(**src.model_dump())
