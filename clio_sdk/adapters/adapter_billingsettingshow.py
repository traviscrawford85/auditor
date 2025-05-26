# Adapter for billingsettingshow
from clio_sdk.models.billingsettingshow import BillingsettingshowIn, BillingsettingshowOut, BillingsettingshowUpdate, BillingsettingshowDb
from clio_client.models import billing_setting_show

def convert_sdk_to_billingsettingshowout(src: billing_setting_show) -> BillingsettingshowOut:
    return BillingsettingshowOut(**src.dict())

def convert_billingsettingshowin_to_sdk(src: BillingsettingshowIn) -> billing_setting_show:
    return billing_setting_show(**src.dict())
