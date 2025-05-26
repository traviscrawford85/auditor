# Adapter for billableclientbase
from clio_sdk.models.billableclientbase import BillableclientbaseIn, BillableclientbaseOut, BillableclientbaseUpdate, BillableclientbaseDb
from clio_client.models import billable_client

def convert_sdk_to_billableclientbaseout(src: billable_client) -> BillableclientbaseOut:
    return BillableclientbaseOut(**src.dict())

def convert_billableclientbasein_to_sdk(src: BillableclientbaseIn) -> billable_client:
    return billable_client(**src.dict())
