# Adapter for expensecategorybase
from clio_sdk.models.expensecategorybase import ExpensecategoryBaseIn, ExpensecategorybaseOut, ExpensecategorybaseUpdate, ExpensecategorybaseDb
from clio_client.models.expense_category import ExpenseCategory

def convert_sdk_to_expensecategorybaseout(src: ExpenseCategory) -> ExpensecategorybaseOut:
    """Converts a clio_client model to clio_sdk model."""
    return ExpensecategorybaseOut(**src.model_dump())

def convert_expensecategorybasein_to_sdk(src: ExpensecategoryBaseIn) -> ExpenseCategory:
    """Converts a clio_sdk model to clio_client model."""
    return ExpenseCategory(**src.model_dump())
