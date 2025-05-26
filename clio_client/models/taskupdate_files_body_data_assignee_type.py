from typing import Literal, cast

TaskupdateFilesBodyDataAssigneeType = Literal["Contact", "User"]

TASKUPDATE_FILES_BODY_DATA_ASSIGNEE_TYPE_VALUES: set[TaskupdateFilesBodyDataAssigneeType] = {
    "Contact",
    "User",
}


def check_taskupdate_files_body_data_assignee_type(value: str) -> TaskupdateFilesBodyDataAssigneeType:
    if value in TASKUPDATE_FILES_BODY_DATA_ASSIGNEE_TYPE_VALUES:
        return cast(TaskupdateFilesBodyDataAssigneeType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKUPDATE_FILES_BODY_DATA_ASSIGNEE_TYPE_VALUES!r}")
