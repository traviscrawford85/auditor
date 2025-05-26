# Adapter for grantlist
from clio_sdk.models.grantlist import GrantlistIn, GrantlistOut, GrantlistUpdate, GrantlistDb
from clio_client.models import grant_list

def convert_sdk_to_grantlistout(src: grant_list) -> GrantlistOut:
    return GrantlistOut(**src.dict())

def convert_grantlistin_to_sdk(src: GrantlistIn) -> grant_list:
    return grant_list(**src.dict())
