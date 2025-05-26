from typing import Literal, cast

TaskupdateFilesBodyDataPriority = Literal["High", "Low", "Normal"]

TASKUPDATE_FILES_BODY_DATA_PRIORITY_VALUES: set[TaskupdateFilesBodyDataPriority] = {
    "High",
    "Low",
    "Normal",
}


def check_taskupdate_files_body_data_priority(value: str) -> TaskupdateFilesBodyDataPriority:
    if value in TASKUPDATE_FILES_BODY_DATA_PRIORITY_VALUES:
        return cast(TaskupdateFilesBodyDataPriority, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKUPDATE_FILES_BODY_DATA_PRIORITY_VALUES!r}")
