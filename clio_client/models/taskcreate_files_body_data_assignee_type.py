from typing import Literal, cast

TaskcreateFilesBodyDataAssigneeType = Literal["Contact", "User"]

TASKCREATE_FILES_BODY_DATA_ASSIGNEE_TYPE_VALUES: set[TaskcreateFilesBodyDataAssigneeType] = {
    "Contact",
    "User",
}


def check_taskcreate_files_body_data_assignee_type(value: str) -> TaskcreateFilesBodyDataAssigneeType:
    if value in TASKCREATE_FILES_BODY_DATA_ASSIGNEE_TYPE_VALUES:
        return cast(TaskcreateFilesBodyDataAssigneeType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKCREATE_FILES_BODY_DATA_ASSIGNEE_TYPE_VALUES!r}")
