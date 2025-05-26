# Adapter for bankaccountbase
from clio_sdk.models.bankaccountbase import BankaccountbaseIn, BankaccountbaseOut, BankaccountbaseUpdate, BankaccountbaseDb
from clio_client.models import bank_account

def convert_sdk_to_bankaccountbaseout(src: bank_account) -> BankaccountbaseOut:
    return BankaccountbaseOut(**src.dict())

def convert_bankaccountbasein_to_sdk(src: BankaccountbaseIn) -> bank_account:
    return bank_account(**src.dict())
