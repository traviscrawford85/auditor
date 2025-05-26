from typing import Literal, cast

ExpenseCategorycreateDataBodyDataEntryType = Literal["hard_cost", "soft_cost", "unassociated"]

EXPENSE_CATEGORYCREATE_DATA_BODY_DATA_ENTRY_TYPE_VALUES: set[ExpenseCategorycreateDataBodyDataEntryType] = {
    "hard_cost",
    "soft_cost",
    "unassociated",
}


def check_expense_categorycreate_data_body_data_entry_type(value: str) -> ExpenseCategorycreateDataBodyDataEntryType:
    if value in EXPENSE_CATEGORYCREATE_DATA_BODY_DATA_ENTRY_TYPE_VALUES:
        return cast(ExpenseCategorycreateDataBodyDataEntryType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXPENSE_CATEGORYCREATE_DATA_BODY_DATA_ENTRY_TYPE_VALUES!r}"
    )
