# Adapter for billingsettingbase
from clio_sdk.models.billingsettingbase import BillingsettingbaseIn, BillingsettingbaseOut, BillingsettingbaseUpdate, BillingsettingbaseDb
from clio_client.models import billing_setting

def convert_sdk_to_billingsettingbaseout(src: billing_setting) -> BillingsettingbaseOut:
    return BillingsettingbaseOut(**src.dict())

def convert_billingsettingbasein_to_sdk(src: BillingsettingbaseIn) -> billing_setting:
    return billing_setting(**src.dict())
