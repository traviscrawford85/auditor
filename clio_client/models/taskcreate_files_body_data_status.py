from typing import Literal, cast

TaskcreateFilesBodyDataStatus = Literal["complete", "in_progress", "in_review", "pending"]

TASKCREATE_FILES_BODY_DATA_STATUS_VALUES: set[TaskcreateFilesBodyDataStatus] = {
    "complete",
    "in_progress",
    "in_review",
    "pending",
}


def check_taskcreate_files_body_data_status(value: str) -> TaskcreateFilesBodyDataStatus:
    if value in TASKCREATE_FILES_BODY_DATA_STATUS_VALUES:
        return cast(TaskcreateFilesBodyDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKCREATE_FILES_BODY_DATA_STATUS_VALUES!r}")
