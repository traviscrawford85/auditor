# Adapter for billshow
from clio_sdk.models.billshow import BillshowIn, BillshowOut, BillshowUpdate, BillshowDb
from clio_client.models.bill_show import BillShow

def convert_sdk_to_billshowout(src: BillShow) -> BillshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return BillshowOut(**src.model_dump())

def convert_billshowin_to_sdk(src: BillshowIn) -> BillShow:
    """Converts a clio_sdk model to clio_client model."""
    return BillShow(**src.model_dump())
