# Adapter for grantfundingsourceshow
from clio_sdk.models.grantfundingsourceshow import GrantfundingsourceshowIn, GrantfundingsourceshowOut, GrantfundingsourceshowUpdate, GrantfundingsourceshowDb
from clio_client.models.grant_funding_source_show import GrantFundingSourceShow

def convert_sdk_to_grantfundingsourceshowout(src: GrantFundingSourceShow) -> GrantfundingsourceshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return GrantfundingsourceshowOut(**src.model_dump())

def convert_grantfundingsourceshowin_to_sdk(src: GrantfundingsourceshowIn) -> GrantFundingSourceShow:
    """Converts a clio_sdk model to clio_client model."""
    return GrantFundingSourceShow(**src.model_dump())
