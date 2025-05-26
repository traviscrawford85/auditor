# Adapter for bankaccountlist
from clio_sdk.models.bankaccountlist import BankaccountlistIn, BankaccountlistOut, BankaccountlistUpdate, BankaccountlistDb
from clio_client.models.bank_account_list import BankAccountList

def convert_sdk_to_bankaccountlistout(src: BankAccountList) -> BankaccountlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return BankaccountlistOut(**src.model_dump())

def convert_bankaccountlistin_to_sdk(src: BankaccountlistIn) -> BankAccountList:
    """Converts a clio_sdk model to clio_client model."""
    return BankAccountList(**src.model_dump())
