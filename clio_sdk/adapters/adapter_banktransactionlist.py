# Adapter for banktransactionlist
from clio_sdk.models.banktransactionlist import BanktransactionlistIn, BanktransactionlistOut, BanktransactionlistUpdate, BanktransactionlistDb
from clio_client.models.bank_transaction_list import BankTransactionList

def convert_sdk_to_banktransactionlistout(src: BankTransactionList) -> BanktransactionlistOut:
    """Converts a clio_client model to clio_sdk model."""
    return BanktransactionlistOut(**src.model_dump())

def convert_banktransactionlistin_to_sdk(src: BanktransactionlistIn) -> BankTransactionList:
    """Converts a clio_sdk model to clio_client model."""
    return BankTransactionList(**src.model_dump())
