# Adapter for billableclientlist
from clio_sdk.models.billableclientlist import BillableclientlistIn, BillableclientlistOut, BillableclientlistUpdate, BillableclientlistDb
from clio_client.models.billable_client_list import BillableClientList

def convert_sdk_to_billableclientlistout(src: BillableClientList) -> BillableclientlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return BillableclientlistOut(**src.model_dump())

def convert_billableclientlistin_to_sdk(src: BillableclientlistIn) -> BillableClientList:
    """Converts a clio_sdk model to clio_client model."""
    return BillableClientList(**src.model_dump())
