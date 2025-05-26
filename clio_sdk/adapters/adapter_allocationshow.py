# Adapter for allocationshow
from clio_sdk.models.allocationshow import AllocationshowIn, AllocationshowOut, AllocationshowUpdate, AllocationshowDb
from clio_client.models import allocation_show

def convert_sdk_to_allocationshowout(src: allocation_show) -> AllocationshowOut:
    return AllocationshowOut(**src.dict())

def convert_allocationshowin_to_sdk(src: AllocationshowIn) -> allocation_show:
    return allocation_show(**src.dict())
