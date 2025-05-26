# Adapter for billthemebase
from clio_sdk.models.billthemebase import BillthemebaseIn, BillthemebaseOut, BillthemebaseUpdate, BillthemebaseDb
from clio_client.models import bill_theme

def convert_sdk_to_billthemebaseout(src: bill_theme) -> BillthemebaseOut:
    return BillthemebaseOut(**src.dict())

def convert_billthemebasein_to_sdk(src: BillthemebaseIn) -> bill_theme:
    return bill_theme(**src.dict())
