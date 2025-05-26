# Adapter for bankaccountshow
from clio_sdk.models.bankaccountshow import BankaccountshowIn, BankaccountshowOut, BankaccountshowUpdate, BankaccountshowDb
from clio_client.models.bank_account_show import BankAccountShow

def convert_sdk_to_bankaccountshowout(src: BankAccountShow) -> BankaccountshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return BankaccountshowOut(**src.model_dump())

def convert_bankaccountshowin_to_sdk(src: BankaccountshowIn) -> BankAccountShow:
    """Converts a clio_sdk model to clio_client model."""
    return BankAccountShow(**src.model_dump())
