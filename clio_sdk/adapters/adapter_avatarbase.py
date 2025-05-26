# Adapter for avatarbase
from clio_sdk.models.avatarbase import AvatarbaseIn, AvatarbaseOut, AvatarbaseUpdate, AvatarbaseDb
from clio_client.models import user_avatar

def convert_sdk_to_avatarbaseout(src: user_avatar) -> AvatarbaseOut:
    return AvatarbaseOut(**src.dict())

def convert_avatarbasein_to_sdk(src: AvatarbaseIn) -> user_avatar:
    return user_avatar(**src.dict())
