from typing import Literal, cast

TaskcreateFilesBodyDataPriority = Literal["High", "Low", "Normal"]

TASKCREATE_FILES_BODY_DATA_PRIORITY_VALUES: set[TaskcreateFilesBodyDataPriority] = {
    "High",
    "Low",
    "Normal",
}


def check_taskcreate_files_body_data_priority(value: str) -> TaskcreateFilesBodyDataPriority:
    if value in TASKCREATE_FILES_BODY_DATA_PRIORITY_VALUES:
        return cast(TaskcreateFilesBodyDataPriority, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKCREATE_FILES_BODY_DATA_PRIORITY_VALUES!r}")
