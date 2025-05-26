from typing import Literal, cast

TaskupdateFilesBodyDataStatus = Literal["complete", "in_progress", "in_review", "pending"]

TASKUPDATE_FILES_BODY_DATA_STATUS_VALUES: set[TaskupdateFilesBodyDataStatus] = {
    "complete",
    "in_progress",
    "in_review",
    "pending",
}


def check_taskupdate_files_body_data_status(value: str) -> TaskupdateFilesBodyDataStatus:
    if value in TASKUPDATE_FILES_BODY_DATA_STATUS_VALUES:
        return cast(TaskupdateFilesBodyDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKUPDATE_FILES_BODY_DATA_STATUS_VALUES!r}")
