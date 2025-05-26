# Adapter for currencybase
from clio_sdk.models.currencybase import CurrencybaseIn, CurrencybaseOut, CurrencybaseUpdate, CurrencybaseDb
from clio_client.models import currency

def convert_sdk_to_currencybaseout(src: currency) -> CurrencybaseOut:
    return CurrencybaseOut(**src.dict())

def convert_currencybasein_to_sdk(src: CurrencybaseIn) -> currency:
    return currency(**src.dict())
