# Adapter for billablematterbase
from clio_sdk.models.billablematterbase import BillablematterbaseIn, BillablematterbaseOut, BillablematterbaseUpdate, BillablematterbaseDb
from clio_client.models import billable_matter

def convert_sdk_to_billablematterbaseout(src: billable_matter) -> BillablematterbaseOut:
    return BillablematterbaseOut(**src.dict())

def convert_billablematterbasein_to_sdk(src: BillablematterbaseIn) -> billable_matter:
    return billable_matter(**src.dict())
