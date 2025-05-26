# Adapter for banktransactionbase
from clio_sdk.models.banktransactionbase import BanktransactionBaseIn, BanktransactionbaseOut, BanktransactionbaseUpdate, BanktransactionbaseDb
from clio_client.models.bank_transaction import BankTransaction

def convert_sdk_to_banktransactionbaseout(src: BankTransaction) -> BanktransactionbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return BanktransactionbaseOut(**src.model_dump())

def convert_banktransactionbasein_to_sdk(src: BanktransactionBaseIn) -> BankTransaction:
    """Converts a clio_sdk model to clio_client model."""
    return BankTransaction(**src.model_dump())
