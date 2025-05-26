# Adapter for userlist
from clio_sdk.models.userlist import UserlistIn, UserlistOut, UserlistUpdate, UserlistDb
from clio_client.models import user_list

def convert_sdk_to_userlistout(src: user_list) -> UserlistOut:
    return UserlistOut(**src.dict())

def convert_userlistin_to_sdk(src: UserlistIn) -> user_list:
    return user_list(**src.dict())
