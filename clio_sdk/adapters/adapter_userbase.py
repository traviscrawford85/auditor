# Adapter for userbase
from clio_sdk.models.userbase import UserBaseIn, UserbaseOut, UserbaseUpdate, UserbaseDb
from clio_client.models.user import User

def convert_sdk_to_userbaseout(src: User) -> UserbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return UserbaseOut(**src.model_dump())

def convert_userbasein_to_sdk(src: UserBaseIn) -> User:
    """Converts a clio_sdk model to clio_client model."""
    return User(**src.model_dump())
