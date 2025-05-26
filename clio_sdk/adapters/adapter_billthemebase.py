# Adapter for billthemebase
from clio_sdk.models.billthemebase import BillthemeBaseIn, BillthemebaseOut, BillthemebaseUpdate, BillthemebaseDb
from clio_client.models.bill_theme import BillTheme

def convert_sdk_to_billthemebaseout(src: BillTheme) -> BillthemebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return BillthemebaseOut(**src.model_dump())

def convert_billthemebasein_to_sdk(src: BillthemeBaseIn) -> BillTheme:
    """Converts a clio_sdk model to clio_client model."""
    return BillTheme(**src.model_dump())
