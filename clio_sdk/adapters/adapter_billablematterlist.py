# Adapter for billablematterlist
from clio_sdk.models.billablematterlist import BillablematterlistIn, BillablematterlistOut, BillablematterlistUpdate, BillablematterlistDb
from clio_client.models.billable_matter_list import BillableMatterList

def convert_sdk_to_billablematterlistout(src: BillableMatterList) -> BillablematterlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return BillablematterlistOut(**src.model_dump())

def convert_billablematterlistin_to_sdk(src: BillablematterlistIn) -> BillableMatterList:
    """Converts a clio_sdk model to clio_client model."""
    return BillableMatterList(**src.model_dump())
