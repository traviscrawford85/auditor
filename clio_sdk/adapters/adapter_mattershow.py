# Adapter for mattershow
from clio_sdk.models.mattershow import MattershowIn, MattershowOut, MattershowUpdate, MattershowDb
from clio_client.models import matter_show

def convert_sdk_to_mattershowout(src: matter_show) -> MattershowOut:
    return MattershowOut(**src.dict())

def convert_mattershowin_to_sdk(src: MattershowIn) -> matter_show:
    return matter_show(**src.dict())
