from typing import Literal, cast

TaskupdateFilesBodyDataPermission = Literal["private", "public"]

TASKUPDATE_FILES_BODY_DATA_PERMISSION_VALUES: set[TaskupdateFilesBodyDataPermission] = {
    "private",
    "public",
}


def check_taskupdate_files_body_data_permission(value: str) -> TaskupdateFilesBodyDataPermission:
    if value in TASKUPDATE_FILES_BODY_DATA_PERMISSION_VALUES:
        return cast(TaskupdateFilesBodyDataPermission, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKUPDATE_FILES_BODY_DATA_PERMISSION_VALUES!r}")
