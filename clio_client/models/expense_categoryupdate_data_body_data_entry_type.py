from typing import Literal, cast

ExpenseCategoryupdateDataBodyDataEntryType = Literal["hard_cost", "soft_cost", "unassociated"]

EXPENSE_CATEGORYUPDATE_DATA_BODY_DATA_ENTRY_TYPE_VALUES: set[ExpenseCategoryupdateDataBodyDataEntryType] = {
    "hard_cost",
    "soft_cost",
    "unassociated",
}


def check_expense_categoryupdate_data_body_data_entry_type(value: str) -> ExpenseCategoryupdateDataBodyDataEntryType:
    if value in EXPENSE_CATEGORYUPDATE_DATA_BODY_DATA_ENTRY_TYPE_VALUES:
        return cast(ExpenseCategoryupdateDataBodyDataEntryType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXPENSE_CATEGORYUPDATE_DATA_BODY_DATA_ENTRY_TYPE_VALUES!r}"
    )
