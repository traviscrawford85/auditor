from typing import Literal, cast

ExpenseCategoryindexOrder = Literal[
    "entry_type(asc)", "entry_type(desc)", "id(asc)", "id(desc)", "name(asc)", "name(desc)", "rate(asc)", "rate(desc)"
]

EXPENSE_CATEGORYINDEX_ORDER_VALUES: set[ExpenseCategoryindexOrder] = {
    "entry_type(asc)",
    "entry_type(desc)",
    "id(asc)",
    "id(desc)",
    "name(asc)",
    "name(desc)",
    "rate(asc)",
    "rate(desc)",
}


def check_expense_categoryindex_order(value: str) -> ExpenseCategoryindexOrder:
    if value in EXPENSE_CATEGORYINDEX_ORDER_VALUES:
        return cast(ExpenseCategoryindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EXPENSE_CATEGORYINDEX_ORDER_VALUES!r}")
