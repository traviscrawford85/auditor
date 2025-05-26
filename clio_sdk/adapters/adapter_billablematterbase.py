# Adapter for billablematterbase
from clio_sdk.models.billablematterbase import BillablematterBaseIn, BillablematterbaseOut, BillablematterbaseUpdate, BillablematterbaseDb
from clio_client.models.billable_matter import BillableMatter

def convert_sdk_to_billablematterbaseout(src: BillableMatter) -> BillablematterbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return BillablematterbaseOut(**src.model_dump())

def convert_billablematterbasein_to_sdk(src: BillablematterBaseIn) -> BillableMatter:
    """Converts a clio_sdk model to clio_client model."""
    return BillableMatter(**src.model_dump())
