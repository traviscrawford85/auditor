# Adapter for billableclientbase
from clio_sdk.models.billableclientbase import BillableclientBaseIn, BillableclientbaseOut, BillableclientbaseUpdate, BillableclientbaseDb
from clio_client.models.billable_client import BillableClient

def convert_sdk_to_billableclientbaseout(src: BillableClient) -> BillableclientbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return BillableclientbaseOut(**src.model_dump())

def convert_billableclientbasein_to_sdk(src: BillableclientBaseIn) -> BillableClient:
    """Converts a clio_sdk model to clio_client model."""
    return BillableClient(**src.model_dump())
