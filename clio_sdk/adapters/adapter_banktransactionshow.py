# Adapter for banktransactionshow
from clio_sdk.models.banktransactionshow import BanktransactionshowIn, BanktransactionshowOut, BanktransactionshowUpdate, BanktransactionshowDb
from clio_client.models import bank_transaction_show

def convert_sdk_to_banktransactionshowout(src: bank_transaction_show) -> BanktransactionshowOut:
    return BanktransactionshowOut(**src.dict())

def convert_banktransactionshowin_to_sdk(src: BanktransactionshowIn) -> bank_transaction_show:
    return bank_transaction_show(**src.dict())
