from typing import Literal, cast

TaskTemplatecreateFilesBodyDataPriority = Literal["High", "Low", "Normal"]

TASK_TEMPLATECREATE_FILES_BODY_DATA_PRIORITY_VALUES: set[TaskTemplatecreateFilesBodyDataPriority] = {
    "High",
    "Low",
    "Normal",
}


def check_task_templatecreate_files_body_data_priority(value: str) -> TaskTemplatecreateFilesBodyDataPriority:
    if value in TASK_TEMPLATECREATE_FILES_BODY_DATA_PRIORITY_VALUES:
        return cast(TaskTemplatecreateFilesBodyDataPriority, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATECREATE_FILES_BODY_DATA_PRIORITY_VALUES!r}"
    )
