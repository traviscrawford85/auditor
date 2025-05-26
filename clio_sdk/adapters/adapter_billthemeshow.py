# Adapter for billthemeshow
from clio_sdk.models.billthemeshow import BillthemeshowIn, BillthemeshowOut, BillthemeshowUpdate, BillthemeshowDb
from clio_client.models import bill_theme_show

def convert_sdk_to_billthemeshowout(src: bill_theme_show) -> BillthemeshowOut:
    return BillthemeshowOut(**src.dict())

def convert_billthemeshowin_to_sdk(src: BillthemeshowIn) -> bill_theme_show:
    return bill_theme_show(**src.dict())
