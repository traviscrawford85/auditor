# Adapter for avatarbase
from clio_sdk.models.avatarbase import AvatarBaseIn, AvatarbaseOut, AvatarbaseUpdate, AvatarbaseDb
from clio_client.models.user_avatar import UserAvatar

def convert_sdk_to_avatarbaseout(src: UserAvatar) -> AvatarbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return AvatarbaseOut(**src.model_dump())

def convert_avatarbasein_to_sdk(src: AvatarBaseIn) -> UserAvatar:
    """Converts a clio_sdk model to clio_client model."""
    return UserAvatar(**src.model_dump())
