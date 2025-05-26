# Adapter for billablemattershow
from clio_sdk.models.billablemattershow import BillablemattershowIn, BillablemattershowOut, BillablemattershowUpdate, BillablemattershowDb
from clio_client.models.billable_matter_show import BillableMatterShow

def convert_sdk_to_billablemattershowout(src: BillableMatterShow) -> BillablemattershowOut:
    """Converts a clio_client model to clio_sdk model."""
    return BillablemattershowOut(**src.model_dump())

def convert_billablemattershowin_to_sdk(src: BillablemattershowIn) -> BillableMatterShow:
    """Converts a clio_sdk model to clio_client model."""
    return BillableMatterShow(**src.model_dump())
