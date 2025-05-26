# Adapter for laukexpensecategorylist
from clio_sdk.models.laukexpensecategorylist import LaukexpensecategorylistIn, LaukexpensecategorylistOut, LaukexpensecategorylistUpdate, LaukexpensecategorylistDb
from clio_client.models import lauk_expense_category_list

def convert_sdk_to_laukexpensecategorylistout(src: lauk_expense_category_list) -> LaukexpensecategorylistOut:
    return LaukexpensecategorylistOut(**src.dict())

def convert_laukexpensecategorylistin_to_sdk(src: LaukexpensecategorylistIn) -> lauk_expense_category_list:
    return lauk_expense_category_list(**src.dict())
