# Adapter for banktransactionlist
from clio_sdk.models.banktransactionlist import BanktransactionlistIn, BanktransactionlistOut, BanktransactionlistUpdate, BanktransactionlistDb
from clio_client.models import bank_transaction_list

def convert_sdk_to_banktransactionlistout(src: bank_transaction_list) -> BanktransactionlistOut:
    return BanktransactionlistOut(**src.dict())

def convert_banktransactionlistin_to_sdk(src: BanktransactionlistIn) -> bank_transaction_list:
    return bank_transaction_list(**src.dict())
