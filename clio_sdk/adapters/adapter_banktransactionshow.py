# Adapter for banktransactionshow
from clio_sdk.models.banktransactionshow import BanktransactionshowIn, BanktransactionshowOut, BanktransactionshowUpdate, BanktransactionshowDb
from clio_client.models.bank_transaction_show import BankTransactionShow

def convert_sdk_to_banktransactionshowout(src: BankTransactionShow) -> BanktransactionshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return BanktransactionshowOut(**src.model_dump())

def convert_banktransactionshowin_to_sdk(src: BanktransactionshowIn) -> BankTransactionShow:
    """Converts a clio_sdk model to clio_client model."""
    return BankTransactionShow(**src.model_dump())
