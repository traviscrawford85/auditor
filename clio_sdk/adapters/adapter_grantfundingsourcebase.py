# Adapter for grantfundingsourcebase
from clio_sdk.models.grantfundingsourcebase import GrantfundingsourceBaseIn, GrantfundingsourcebaseOut, GrantfundingsourcebaseUpdate, GrantfundingsourcebaseDb
from clio_client.models.grant_funding_source import GrantFundingSource

def convert_sdk_to_grantfundingsourcebaseout(src: GrantFundingSource) -> GrantfundingsourcebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return GrantfundingsourcebaseOut(**src.model_dump())

def convert_grantfundingsourcebasein_to_sdk(src: GrantfundingsourceBaseIn) -> GrantFundingSource:
    """Converts a clio_sdk model to clio_client model."""
    return GrantFundingSource(**src.model_dump())
