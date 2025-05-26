# Adapter for bankaccountbase
from clio_sdk.models.bankaccountbase import BankaccountBaseIn, BankaccountbaseOut, BankaccountbaseUpdate, BankaccountbaseDb
from clio_client.models.bank_account import BankAccount

def convert_sdk_to_bankaccountbaseout(src: BankAccount) -> BankaccountbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return BankaccountbaseOut(**src.model_dump())

def convert_bankaccountbasein_to_sdk(src: BankaccountBaseIn) -> BankAccount:
    """Converts a clio_sdk model to clio_client model."""
    return BankAccount(**src.model_dump())
