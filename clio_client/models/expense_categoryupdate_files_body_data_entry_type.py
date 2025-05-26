from typing import Literal, cast

ExpenseCategoryupdateFilesBodyDataEntryType = Literal["hard_cost", "soft_cost", "unassociated"]

EXPENSE_CATEGORYUPDATE_FILES_BODY_DATA_ENTRY_TYPE_VALUES: set[ExpenseCategoryupdateFilesBodyDataEntryType] = {
    "hard_cost",
    "soft_cost",
    "unassociated",
}


def check_expense_categoryupdate_files_body_data_entry_type(value: str) -> ExpenseCategoryupdateFilesBodyDataEntryType:
    if value in EXPENSE_CATEGORYUPDATE_FILES_BODY_DATA_ENTRY_TYPE_VALUES:
        return cast(ExpenseCategoryupdateFilesBodyDataEntryType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXPENSE_CATEGORYUPDATE_FILES_BODY_DATA_ENTRY_TYPE_VALUES!r}"
    )
