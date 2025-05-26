from typing import Literal, cast

ActivitycreateFilesBodyDataType = Literal["ExpenseEntry", "HardCostEntry", "SoftCostEntry", "TimeEntry"]

ACTIVITYCREATE_FILES_BODY_DATA_TYPE_VALUES: set[ActivitycreateFilesBodyDataType] = {
    "ExpenseEntry",
    "HardCostEntry",
    "SoftCostEntry",
    "TimeEntry",
}


def check_activitycreate_files_body_data_type(value: str) -> ActivitycreateFilesBodyDataType:
    if value in ACTIVITYCREATE_FILES_BODY_DATA_TYPE_VALUES:
        return cast(ActivitycreateFilesBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITYCREATE_FILES_BODY_DATA_TYPE_VALUES!r}")
