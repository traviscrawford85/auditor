# Adapter for billablemattershow
from clio_sdk.models.billablemattershow import BillablemattershowIn, BillablemattershowOut, BillablemattershowUpdate, BillablemattershowDb
from clio_client.models import billable_matter_show

def convert_sdk_to_billablemattershowout(src: billable_matter_show) -> BillablemattershowOut:
    return BillablemattershowOut(**src.dict())

def convert_billablemattershowin_to_sdk(src: BillablemattershowIn) -> billable_matter_show:
    return billable_matter_show(**src.dict())
