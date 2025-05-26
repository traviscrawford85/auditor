# Adapter for accountbase
from clio_sdk.models.accountbase import AccountbaseIn, AccountbaseOut, AccountbaseUpdate, AccountbaseDb
from clio_client.models import user_account

def convert_sdk_to_accountbaseout(src: user_account) -> AccountbaseOut:
    return AccountbaseOut(**src.dict())

def convert_accountbasein_to_sdk(src: AccountbaseIn) -> user_account:
    return user_account(**src.dict())
