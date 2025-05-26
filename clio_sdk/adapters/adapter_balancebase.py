# Adapter for balancebase
from clio_sdk.models.balancebase import BalancebaseIn, BalancebaseOut, BalancebaseUpdate, BalancebaseDb
from clio_client.models import balance_base

def convert_sdk_to_balancebaseout(src: balance_base) -> BalancebaseOut:
    return BalancebaseOut(**src.dict())

def convert_balancebasein_to_sdk(src: BalancebaseIn) -> balance_base:
    return balance_base(**src.dict())
