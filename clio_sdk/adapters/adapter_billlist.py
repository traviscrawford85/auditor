# Adapter for billlist
from clio_sdk.models.billlist import BilllistIn, BilllistOut, BilllistUpdate, BilllistDb
from clio_client.models import bill_list

def convert_sdk_to_billlistout(src: bill_list) -> BilllistOut:
    return BilllistOut(**src.dict())

def convert_billlistin_to_sdk(src: BilllistIn) -> bill_list:
    return bill_list(**src.dict())
