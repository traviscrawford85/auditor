# Adapter for userlist
from clio_sdk.models.userlist import UserlistIn, UserlistOut, UserlistUpdate, UserlistDb
from clio_client.models.user_list import UserList

def convert_sdk_to_userlistout(src: UserList) -> UserlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return UserlistOut(**src.model_dump())

def convert_userlistin_to_sdk(src: UserlistIn) -> UserList:
    """Converts a clio_sdk model to clio_client model."""
    return UserList(**src.model_dump())
