# Adapter for expensecategorylist
from clio_sdk.models.expensecategorylist import ExpensecategorylistIn, ExpensecategorylistOut, ExpensecategorylistUpdate, ExpensecategorylistDb
from clio_client.models.expense_category_list import ExpenseCategoryList

def convert_sdk_to_expensecategorylistout(src: ExpenseCategoryList) -> ExpensecategorylistOut:
    """Converts a clio_client model to clio_sdk model."""
    return ExpensecategorylistOut(**src.model_dump())

def convert_expensecategorylistin_to_sdk(src: ExpensecategorylistIn) -> ExpenseCategoryList:
    """Converts a clio_sdk model to clio_client model."""
    return ExpenseCategoryList(**src.model_dump())
