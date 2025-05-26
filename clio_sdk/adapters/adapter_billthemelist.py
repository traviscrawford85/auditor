# Adapter for billthemelist
from clio_sdk.models.billthemelist import BillthemelistIn, BillthemelistOut, BillthemelistUpdate, BillthemelistDb
from clio_client.models import bill_theme_list

def convert_sdk_to_billthemelistout(src: bill_theme_list) -> BillthemelistOut:
    return BillthemelistOut(**src.dict())

def convert_billthemelistin_to_sdk(src: BillthemelistIn) -> bill_theme_list:
    return bill_theme_list(**src.dict())
