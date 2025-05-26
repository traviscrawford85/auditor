# Adapter for grantfundingsourcelist
from clio_sdk.models.grantfundingsourcelist import GrantfundingsourcelistIn, GrantfundingsourcelistOut, GrantfundingsourcelistUpdate, GrantfundingsourcelistDb
from clio_client.models.grant_funding_source_list import GrantFundingSourceList

def convert_sdk_to_grantfundingsourcelistout(src: GrantFundingSourceList) -> GrantfundingsourcelistOut:
    """Converts a clio_client model to clio_sdk model."""
    return GrantfundingsourcelistOut(**src.model_dump())

def convert_grantfundingsourcelistin_to_sdk(src: GrantfundingsourcelistIn) -> GrantFundingSourceList:
    """Converts a clio_sdk model to clio_client model."""
    return GrantFundingSourceList(**src.model_dump())
