from typing import Literal, cast

TaskTemplateupdateFilesBodyDataPriority = Literal["High", "Low", "Normal"]

TASK_TEMPLATEUPDATE_FILES_BODY_DATA_PRIORITY_VALUES: set[TaskTemplateupdateFilesBodyDataPriority] = {
    "High",
    "Low",
    "Normal",
}


def check_task_templateupdate_files_body_data_priority(value: str) -> TaskTemplateupdateFilesBodyDataPriority:
    if value in TASK_TEMPLATEUPDATE_FILES_BODY_DATA_PRIORITY_VALUES:
        return cast(TaskTemplateupdateFilesBodyDataPriority, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATEUPDATE_FILES_BODY_DATA_PRIORITY_VALUES!r}"
    )
