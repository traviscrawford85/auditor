# Adapter for usershow
from clio_sdk.models.usershow import UsershowIn, UsershowOut, UsershowUpdate, UsershowDb
from clio_client.models import user_show

def convert_sdk_to_usershowout(src: user_show) -> UsershowOut:
    return UsershowOut(**src.dict())

def convert_usershowin_to_sdk(src: UsershowIn) -> user_show:
    return user_show(**src.dict())
