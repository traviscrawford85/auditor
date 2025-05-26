# Adapter for balancebase
from clio_sdk.models.balancebase import BalanceBaseIn, BalancebaseOut, BalancebaseUpdate, BalancebaseDb
from clio_client.models.balance_base import BalanceBase

def convert_sdk_to_balancebaseout(src: BalanceBase) -> BalancebaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return BalancebaseOut(**src.model_dump())

def convert_balancebasein_to_sdk(src: BalanceBaseIn) -> BalanceBase:
    """Converts a clio_sdk model to clio_client model."""
    return BalanceBase(**src.model_dump())
