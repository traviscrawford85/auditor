# Adapter for expensecategoryshow
from clio_sdk.models.expensecategoryshow import ExpensecategoryshowIn, ExpensecategoryshowOut, ExpensecategoryshowUpdate, ExpensecategoryshowDb
from clio_client.models.expense_category_show import ExpenseCategoryShow

def convert_sdk_to_expensecategoryshowout(src: ExpenseCategoryShow) -> ExpensecategoryshowOut:
    """Converts a clio_client model to clio_sdk model."""
    return ExpensecategoryshowOut(**src.model_dump())

def convert_expensecategoryshowin_to_sdk(src: ExpensecategoryshowIn) -> ExpenseCategoryShow:
    """Converts a clio_sdk model to clio_client model."""
    return ExpenseCategoryShow(**src.model_dump())
