# Adapter for expensecategorybase
from clio_sdk.models.expensecategorybase import ExpensecategorybaseIn, ExpensecategorybaseOut, ExpensecategorybaseUpdate, ExpensecategorybaseDb
from clio_client.models import expense_category

def convert_sdk_to_expensecategorybaseout(src: expense_category) -> ExpensecategorybaseOut:
    return ExpensecategorybaseOut(**src.dict())

def convert_expensecategorybasein_to_sdk(src: ExpensecategorybaseIn) -> expense_category:
    return expense_category(**src.dict())
