from typing import Literal, cast

ExpenseCategoryupdateJsonBodyDataEntryType = Literal["hard_cost", "soft_cost", "unassociated"]

EXPENSE_CATEGORYUPDATE_JSON_BODY_DATA_ENTRY_TYPE_VALUES: set[ExpenseCategoryupdateJsonBodyDataEntryType] = {
    "hard_cost",
    "soft_cost",
    "unassociated",
}


def check_expense_categoryupdate_json_body_data_entry_type(value: str) -> ExpenseCategoryupdateJsonBodyDataEntryType:
    if value in EXPENSE_CATEGORYUPDATE_JSON_BODY_DATA_ENTRY_TYPE_VALUES:
        return cast(ExpenseCategoryupdateJsonBodyDataEntryType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXPENSE_CATEGORYUPDATE_JSON_BODY_DATA_ENTRY_TYPE_VALUES!r}"
    )
