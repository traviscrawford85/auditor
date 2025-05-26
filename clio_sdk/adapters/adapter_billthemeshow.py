# Adapter for billthemeshow
from clio_sdk.models.billthemeshow import BillthemeshowIn, BillthemeshowOut, BillthemeshowUpdate, BillthemeshowDb
from clio_client.models.bill_theme_show import BillThemeShow

def convert_sdk_to_billthemeshowout(src: BillThemeShow) -> BillthemeshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return BillthemeshowOut(**src.model_dump())

def convert_billthemeshowin_to_sdk(src: BillthemeshowIn) -> BillThemeShow:
    """Converts a clio_sdk model to clio_client model."""
    return BillThemeShow(**src.model_dump())
