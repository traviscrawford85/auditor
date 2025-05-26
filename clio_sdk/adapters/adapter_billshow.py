# Adapter for billshow
from clio_sdk.models.billshow import BillshowIn, BillshowOut, BillshowUpdate, BillshowDb
from clio_client.models import bill_show

def convert_sdk_to_billshowout(src: bill_show) -> BillshowOut:
    return BillshowOut(**src.dict())

def convert_billshowin_to_sdk(src: BillshowIn) -> bill_show:
    return bill_show(**src.dict())
