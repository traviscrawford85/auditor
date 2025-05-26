# Adapter for laukexpensecategorylist
from clio_sdk.models.laukexpensecategorylist import LaukexpensecategorylistIn, LaukexpensecategorylistOut, LaukexpensecategorylistUpdate, LaukexpensecategorylistDb
from clio_client.models.lauk_expense_category_list import LaukExpenseCategoryList

def convert_sdk_to_laukexpensecategorylistout(src: LaukExpenseCategoryList) -> LaukexpensecategorylistOut:
    """Converts a clio_client model to clio_sdk model."""
    return LaukexpensecategorylistOut(**src.model_dump())

def convert_laukexpensecategorylistin_to_sdk(src: LaukexpensecategorylistIn) -> LaukExpenseCategoryList:
    """Converts a clio_sdk model to clio_client model."""
    return LaukExpenseCategoryList(**src.model_dump())
