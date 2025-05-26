# Adapter for billableclientlist
from clio_sdk.models.billableclientlist import BillableclientlistIn, BillableclientlistOut, BillableclientlistUpdate, BillableclientlistDb
from clio_client.models import billable_client_list

def convert_sdk_to_billableclientlistout(src: billable_client_list) -> BillableclientlistOut:
    return BillableclientlistOut(**src.dict())

def convert_billableclientlistin_to_sdk(src: BillableclientlistIn) -> billable_client_list:
    return billable_client_list(**src.dict())
