# Adapter for discountbase
from clio_sdk.models.discountbase import DiscountBaseIn, DiscountbaseOut, DiscountbaseUpdate, DiscountbaseDb
from clio_client.models.discount_base import DiscountBase

def convert_sdk_to_discountbaseout(src: DiscountBase) -> DiscountbaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return DiscountbaseOut(**src.model_dump())

def convert_discountbasein_to_sdk(src: DiscountBaseIn) -> DiscountBase:
    """Converts a clio_sdk model to clio_client model."""
    return DiscountBase(**src.model_dump())
