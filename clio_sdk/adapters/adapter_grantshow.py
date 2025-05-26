# Adapter for grantshow
from clio_sdk.models.grantshow import GrantshowIn, GrantshowOut, GrantshowUpdate, GrantshowDb
from clio_client.models import grant_show

def convert_sdk_to_grantshowout(src: grant_show) -> GrantshowOut:
    return GrantshowOut(**src.dict())

def convert_grantshowin_to_sdk(src: GrantshowIn) -> grant_show:
    return grant_show(**src.dict())
