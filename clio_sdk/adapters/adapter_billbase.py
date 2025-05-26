# Adapter for billbase
from clio_sdk.models.billbase import BillbaseIn, BillbaseOut, BillbaseUpdate, BillbaseDb
from clio_client.models import bill

def convert_sdk_to_billbaseout(src: bill) -> BillbaseOut:
    return BillbaseOut(**src.dict())

def convert_billbasein_to_sdk(src: BillbaseIn) -> bill:
    return bill(**src.dict())
