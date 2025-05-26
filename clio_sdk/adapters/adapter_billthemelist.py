# Adapter for billthemelist
from clio_sdk.models.billthemelist import BillthemelistIn, BillthemelistOut, BillthemelistUpdate, BillthemelistDb
from clio_client.models.bill_theme_list import BillThemeList

def convert_sdk_to_billthemelistout(src: BillThemeList) -> BillthemelistOut:
    """Converts a clio_client model to clio_sdk model."""
    return BillthemelistOut(**src.model_dump())

def convert_billthemelistin_to_sdk(src: BillthemelistIn) -> BillThemeList:
    """Converts a clio_sdk model to clio_client model."""
    return BillThemeList(**src.model_dump())
