# Adapter for billlist
from clio_sdk.models.billlist import BilllistIn, BilllistOut, BilllistUpdate, BilllistDb
from clio_client.models.bill_list import BillList

def convert_sdk_to_billlistout(src: BillList) -> BilllistOut:
    """Converts a clio_client model to clio_sdk model."""
    return BilllistOut(**src.model_dump())

def convert_billlistin_to_sdk(src: BilllistIn) -> BillList:
    """Converts a clio_sdk model to clio_client model."""
    return BillList(**src.model_dump())
