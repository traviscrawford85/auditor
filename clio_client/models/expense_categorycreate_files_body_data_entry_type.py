from typing import Literal, cast

ExpenseCategorycreateFilesBodyDataEntryType = Literal["hard_cost", "soft_cost", "unassociated"]

EXPENSE_CATEGORYCREATE_FILES_BODY_DATA_ENTRY_TYPE_VALUES: set[ExpenseCategorycreateFilesBodyDataEntryType] = {
    "hard_cost",
    "soft_cost",
    "unassociated",
}


def check_expense_categorycreate_files_body_data_entry_type(value: str) -> ExpenseCategorycreateFilesBodyDataEntryType:
    if value in EXPENSE_CATEGORYCREATE_FILES_BODY_DATA_ENTRY_TYPE_VALUES:
        return cast(ExpenseCategorycreateFilesBodyDataEntryType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXPENSE_CATEGORYCREATE_FILES_BODY_DATA_ENTRY_TYPE_VALUES!r}"
    )
