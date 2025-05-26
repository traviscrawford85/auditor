# Adapter for usershow
from clio_sdk.models.usershow import UsershowIn, UsershowOut, UsershowUpdate, UsershowDb
from clio_client.models.user_show import UserShow

def convert_sdk_to_usershowout(src: UserShow) -> UsershowOut:
    """Converts a clio_client model to clio_sdk model."""
    return UsershowOut(**src.model_dump())

def convert_usershowin_to_sdk(src: UsershowIn) -> UserShow:
    """Converts a clio_sdk model to clio_client model."""
    return UserShow(**src.model_dump())
