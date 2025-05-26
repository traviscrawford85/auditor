# Adapter for userbase
from clio_sdk.models.userbase import UserbaseIn, UserbaseOut, UserbaseUpdate, UserbaseDb
from clio_client.models import user

def convert_sdk_to_userbaseout(src: user) -> UserbaseOut:
    return UserbaseOut(**src.dict())

def convert_userbasein_to_sdk(src: UserbaseIn) -> user:
    return user(**src.dict())
