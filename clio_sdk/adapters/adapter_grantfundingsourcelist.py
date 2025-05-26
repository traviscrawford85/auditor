# Adapter for grantfundingsourcelist
from clio_sdk.models.grantfundingsourcelist import GrantfundingsourcelistIn, GrantfundingsourcelistOut, GrantfundingsourcelistUpdate, GrantfundingsourcelistDb
from clio_client.models import grant_funding_source_list

def convert_sdk_to_grantfundingsourcelistout(src: grant_funding_source_list) -> GrantfundingsourcelistOut:
    return GrantfundingsourcelistOut(**src.dict())

def convert_grantfundingsourcelistin_to_sdk(src: GrantfundingsourcelistIn) -> grant_funding_source_list:
    return grant_funding_source_list(**src.dict())
