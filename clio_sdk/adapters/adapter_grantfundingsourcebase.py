# Adapter for grantfundingsourcebase
from clio_sdk.models.grantfundingsourcebase import GrantfundingsourcebaseIn, GrantfundingsourcebaseOut, GrantfundingsourcebaseUpdate, GrantfundingsourcebaseDb
from clio_client.models import grant_funding_source

def convert_sdk_to_grantfundingsourcebaseout(src: grant_funding_source) -> GrantfundingsourcebaseOut:
    return GrantfundingsourcebaseOut(**src.dict())

def convert_grantfundingsourcebasein_to_sdk(src: GrantfundingsourcebaseIn) -> grant_funding_source:
    return grant_funding_source(**src.dict())
