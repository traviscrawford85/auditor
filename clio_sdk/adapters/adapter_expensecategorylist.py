# Adapter for expensecategorylist
from clio_sdk.models.expensecategorylist import ExpensecategorylistIn, ExpensecategorylistOut, ExpensecategorylistUpdate, ExpensecategorylistDb
from clio_client.models import expense_category_list

def convert_sdk_to_expensecategorylistout(src: expense_category_list) -> ExpensecategorylistOut:
    return ExpensecategorylistOut(**src.dict())

def convert_expensecategorylistin_to_sdk(src: ExpensecategorylistIn) -> expense_category_list:
    return expense_category_list(**src.dict())
