# Adapter for banktransactionbase
from clio_sdk.models.banktransactionbase import BanktransactionbaseIn, BanktransactionbaseOut, BanktransactionbaseUpdate, BanktransactionbaseDb
from clio_client.models import bank_transaction

def convert_sdk_to_banktransactionbaseout(src: bank_transaction) -> BanktransactionbaseOut:
    return BanktransactionbaseOut(**src.dict())

def convert_banktransactionbasein_to_sdk(src: BanktransactionbaseIn) -> bank_transaction:
    return bank_transaction(**src.dict())
