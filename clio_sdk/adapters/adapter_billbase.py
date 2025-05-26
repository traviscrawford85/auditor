# Adapter for billbase
from clio_sdk.models.billbase import BillBaseIn, BillbaseOut, BillbaseUpdate, BillbaseDb
from clio_client.models.bill import Bill

def convert_sdk_to_billbaseout(src: Bill) -> BillbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return BillbaseOut(**src.model_dump())

def convert_billbasein_to_sdk(src: BillBaseIn) -> Bill:
    """Converts a clio_sdk model to clio_client model."""
    return Bill(**src.model_dump())
