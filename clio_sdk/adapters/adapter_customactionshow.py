# Adapter for customactionshow
from clio_sdk.models.customactionshow import CustomactionshowIn, CustomactionshowOut, CustomactionshowUpdate, CustomactionshowDb
from clio_client.models.custom_action_show import CustomActionShow

def convert_sdk_to_customactionshowout(src: CustomActionShow) -> CustomactionshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return CustomactionshowOut(**src.model_dump())

def convert_customactionshowin_to_sdk(src: CustomactionshowIn) -> CustomActionShow:
    """Converts a clio_sdk model to clio_client model."""
    return CustomActionShow(**src.model_dump())
