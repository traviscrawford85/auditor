# Adapter for accountbalancebase
from clio_sdk.models.accountbalancebase import AccountbalanceBaseIn, AccountbalancebaseOut, AccountbalancebaseUpdate, AccountbalancebaseDb
from clio_client.models.account_balance_base import AccountBalanceBase

def convert_sdk_to_accountbalancebaseout(src: AccountBalanceBase) -> AccountbalancebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return AccountbalancebaseOut(**src.model_dump())

def convert_accountbalancebasein_to_sdk(src: AccountbalanceBaseIn) -> AccountBalanceBase:
    """Converts a clio_sdk model to clio_client model."""
    return AccountBalanceBase(**src.model_dump())
