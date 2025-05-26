# Adapter for accountbalancebase
from clio_sdk.models.accountbalancebase import AccountbalancebaseIn, AccountbalancebaseOut, AccountbalancebaseUpdate, AccountbalancebaseDb
from clio_client.models import account_balance_base

def convert_sdk_to_accountbalancebaseout(src: account_balance_base) -> AccountbalancebaseOut:
    return AccountbalancebaseOut(**src.dict())

def convert_accountbalancebasein_to_sdk(src: AccountbalancebaseIn) -> account_balance_base:
    return account_balance_base(**src.dict())
