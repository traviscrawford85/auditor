# Adapter for laukexpensecategorybase
from clio_sdk.models.laukexpensecategorybase import LaukexpensecategorybaseIn, LaukexpensecategorybaseOut, LaukexpensecategorybaseUpdate, LaukexpensecategorybaseDb
from clio_client.models import lauk_expense_category

def convert_sdk_to_laukexpensecategorybaseout(src: lauk_expense_category) -> LaukexpensecategorybaseOut:
    return LaukexpensecategorybaseOut(**src.dict())

def convert_laukexpensecategorybasein_to_sdk(src: LaukexpensecategorybaseIn) -> lauk_expense_category:
    return lauk_expense_category(**src.dict())
