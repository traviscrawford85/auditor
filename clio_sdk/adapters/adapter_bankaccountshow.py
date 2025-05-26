# Adapter for bankaccountshow
from clio_sdk.models.bankaccountshow import BankaccountshowIn, BankaccountshowOut, BankaccountshowUpdate, BankaccountshowDb
from clio_client.models import bank_account_show

def convert_sdk_to_bankaccountshowout(src: bank_account_show) -> BankaccountshowOut:
    return BankaccountshowOut(**src.dict())

def convert_bankaccountshowin_to_sdk(src: BankaccountshowIn) -> bank_account_show:
    return bank_account_show(**src.dict())
