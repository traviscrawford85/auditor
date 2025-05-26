# Adapter for laukexpensecategorybase
from clio_sdk.models.laukexpensecategorybase import LaukexpensecategoryBaseIn, LaukexpensecategorybaseOut, LaukexpensecategorybaseUpdate, LaukexpensecategorybaseDb
from clio_client.models.lauk_expense_category import LaukExpenseCategory

def convert_sdk_to_laukexpensecategorybaseout(src: LaukExpenseCategory) -> LaukexpensecategorybaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return LaukexpensecategorybaseOut(**src.model_dump())

def convert_laukexpensecategorybasein_to_sdk(src: LaukexpensecategoryBaseIn) -> LaukExpenseCategory:
    """Converts a clio_sdk model to clio_client model."""
    return LaukExpenseCategory(**src.model_dump())
