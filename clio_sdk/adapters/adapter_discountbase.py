# Adapter for discountbase
from clio_sdk.models.discountbase import DiscountbaseIn, DiscountbaseOut, DiscountbaseUpdate, DiscountbaseDb
from clio_client.models import discount_base

def convert_sdk_to_discountbaseout(src: discount_base) -> DiscountbaseOut:
    return DiscountbaseOut(**src.dict())

def convert_discountbasein_to_sdk(src: DiscountbaseIn) -> discount_base:
    return discount_base(**src.dict())
