# Adapter for currencylist
from clio_sdk.models.currencylist import CurrencylistIn, CurrencylistOut, CurrencylistUpdate, CurrencylistDb
from clio_client.models.currency_list import CurrencyList

def convert_sdk_to_currencylistout(src: CurrencyList) -> CurrencylistOut:
    """Converts a clio_client model to clio_sdk model."""
    return CurrencylistOut(**src.model_dump())

def convert_currencylistin_to_sdk(src: CurrencylistIn) -> CurrencyList:
    """Converts a clio_sdk model to clio_client model."""
    return CurrencyList(**src.model_dump())
