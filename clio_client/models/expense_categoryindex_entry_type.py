from typing import Literal, cast

ExpenseCategoryindexEntryType = Literal["hard_cost", "soft_cost", "unassociated"]

EXPENSE_CATEGORYINDEX_ENTRY_TYPE_VALUES: set[ExpenseCategoryindexEntryType] = {
    "hard_cost",
    "soft_cost",
    "unassociated",
}


def check_expense_categoryindex_entry_type(value: str) -> ExpenseCategoryindexEntryType:
    if value in EXPENSE_CATEGORYINDEX_ENTRY_TYPE_VALUES:
        return cast(ExpenseCategoryindexEntryType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EXPENSE_CATEGORYINDEX_ENTRY_TYPE_VALUES!r}")
