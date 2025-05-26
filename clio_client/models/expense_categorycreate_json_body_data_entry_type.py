from typing import Literal, cast

ExpenseCategorycreateJsonBodyDataEntryType = Literal["hard_cost", "soft_cost", "unassociated"]

EXPENSE_CATEGORYCREATE_JSON_BODY_DATA_ENTRY_TYPE_VALUES: set[ExpenseCategorycreateJsonBodyDataEntryType] = {
    "hard_cost",
    "soft_cost",
    "unassociated",
}


def check_expense_categorycreate_json_body_data_entry_type(value: str) -> ExpenseCategorycreateJsonBodyDataEntryType:
    if value in EXPENSE_CATEGORYCREATE_JSON_BODY_DATA_ENTRY_TYPE_VALUES:
        return cast(ExpenseCategorycreateJsonBodyDataEntryType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXPENSE_CATEGORYCREATE_JSON_BODY_DATA_ENTRY_TYPE_VALUES!r}"
    )
