# Adapter for grantlist
from clio_sdk.models.grantlist import GrantlistIn, GrantlistOut, GrantlistUpdate, GrantlistDb
from clio_client.models.grant_list import GrantList

def convert_sdk_to_grantlistout(src: GrantList) -> GrantlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return GrantlistOut(**src.model_dump())

def convert_grantlistin_to_sdk(src: GrantlistIn) -> GrantList:
    """Converts a clio_sdk model to clio_client model."""
    return GrantList(**src.model_dump())
