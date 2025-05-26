# Adapter for billablematterlist
from clio_sdk.models.billablematterlist import BillablematterlistIn, BillablematterlistOut, BillablematterlistUpdate, BillablematterlistDb
from clio_client.models import billable_matter_list

def convert_sdk_to_billablematterlistout(src: billable_matter_list) -> BillablematterlistOut:
    return BillablematterlistOut(**src.dict())

def convert_billablematterlistin_to_sdk(src: BillablematterlistIn) -> billable_matter_list:
    return billable_matter_list(**src.dict())
