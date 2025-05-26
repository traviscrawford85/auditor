# Adapter for grantfundingsourceshow
from clio_sdk.models.grantfundingsourceshow import GrantfundingsourceshowIn, GrantfundingsourceshowOut, GrantfundingsourceshowUpdate, GrantfundingsourceshowDb
from clio_client.models import grant_funding_source_show

def convert_sdk_to_grantfundingsourceshowout(src: grant_funding_source_show) -> GrantfundingsourceshowOut:
    return GrantfundingsourceshowOut(**src.dict())

def convert_grantfundingsourceshowin_to_sdk(src: GrantfundingsourceshowIn) -> grant_funding_source_show:
    return grant_funding_source_show(**src.dict())
