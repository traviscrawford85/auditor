# Adapter for grantshow
from clio_sdk.models.grantshow import GrantshowIn, GrantshowOut, GrantshowUpdate, GrantshowDb
from clio_client.models.grant_show import GrantShow

def convert_sdk_to_grantshowout(src: GrantShow) -> GrantshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return GrantshowOut(**src.model_dump())

def convert_grantshowin_to_sdk(src: GrantshowIn) -> GrantShow:
    """Converts a clio_sdk model to clio_client model."""
    return GrantShow(**src.model_dump())
