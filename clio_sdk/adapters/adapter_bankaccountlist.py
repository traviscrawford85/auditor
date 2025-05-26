# Adapter for bankaccountlist
from clio_sdk.models.bankaccountlist import BankaccountlistIn, BankaccountlistOut, BankaccountlistUpdate, BankaccountlistDb
from clio_client.models import bank_account_list

def convert_sdk_to_bankaccountlistout(src: bank_account_list) -> BankaccountlistOut:
    return BankaccountlistOut(**src.dict())

def convert_bankaccountlistin_to_sdk(src: BankaccountlistIn) -> bank_account_list:
    return bank_account_list(**src.dict())
