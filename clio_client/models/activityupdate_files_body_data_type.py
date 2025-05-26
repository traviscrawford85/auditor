from typing import Literal, cast

ActivityupdateFilesBodyDataType = Literal["ExpenseEntry", "HardCostEntry", "SoftCostEntry", "TimeEntry"]

ACTIVITYUPDATE_FILES_BODY_DATA_TYPE_VALUES: set[ActivityupdateFilesBodyDataType] = {
    "ExpenseEntry",
    "HardCostEntry",
    "SoftCostEntry",
    "TimeEntry",
}


def check_activityupdate_files_body_data_type(value: str) -> ActivityupdateFilesBodyDataType:
    if value in ACTIVITYUPDATE_FILES_BODY_DATA_TYPE_VALUES:
        return cast(ActivityupdateFilesBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITYUPDATE_FILES_BODY_DATA_TYPE_VALUES!r}")
