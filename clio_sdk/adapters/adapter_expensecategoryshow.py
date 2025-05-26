# Adapter for expensecategoryshow
from clio_sdk.models.expensecategoryshow import ExpensecategoryshowIn, ExpensecategoryshowOut, ExpensecategoryshowUpdate, ExpensecategoryshowDb
from clio_client.models import expense_category_show

def convert_sdk_to_expensecategoryshowout(src: expense_category_show) -> ExpensecategoryshowOut:
    return ExpensecategoryshowOut(**src.dict())

def convert_expensecategoryshowin_to_sdk(src: ExpensecategoryshowIn) -> expense_category_show:
    return expense_category_show(**src.dict())
