# Adapter for accountbase
from clio_sdk.models.accountbase import AccountBaseIn, AccountbaseOut, AccountbaseUpdate, AccountbaseDb
from clio_client.models.user_account import UserAccount

def convert_sdk_to_accountbaseout(src: UserAccount) -> AccountbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return AccountbaseOut(**src.model_dump())

def convert_accountbasein_to_sdk(src: AccountBaseIn) -> UserAccount:
    """Converts a clio_sdk model to clio_client model."""
    return UserAccount(**src.model_dump())
