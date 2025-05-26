# Adapter for currencybase
from clio_sdk.models.currencybase import CurrencyBaseIn, CurrencybaseOut, CurrencybaseUpdate, CurrencybaseDb
from clio_client.models.currency import Currency

def convert_sdk_to_currencybaseout(src: Currency) -> CurrencybaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return CurrencybaseOut(**src.model_dump())

def convert_currencybasein_to_sdk(src: CurrencyBaseIn) -> Currency:
    """Converts a clio_sdk model to clio_client model."""
    return Currency(**src.model_dump())
