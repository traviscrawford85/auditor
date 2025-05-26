# Adapter for currencylist
from clio_sdk.models.currencylist import CurrencylistIn, CurrencylistOut, CurrencylistUpdate, CurrencylistDb
from clio_client.models import currency_list

def convert_sdk_to_currencylistout(src: currency_list) -> CurrencylistOut:
    return CurrencylistOut(**src.dict())

def convert_currencylistin_to_sdk(src: CurrencylistIn) -> currency_list:
    return currency_list(**src.dict())
