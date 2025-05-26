# Adapter for allocationshow
from clio_sdk.models.allocationshow import AllocationshowIn, AllocationshowOut, AllocationshowUpdate, AllocationshowDb
from clio_client.models.allocation_show import AllocationShow

def convert_sdk_to_allocationshowout(src: AllocationShow) -> AllocationshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return AllocationshowOut(**src.model_dump())

def convert_allocationshowin_to_sdk(src: AllocationshowIn) -> AllocationShow:
    """Converts a clio_sdk model to clio_client model."""
    return AllocationShow(**src.model_dump())
