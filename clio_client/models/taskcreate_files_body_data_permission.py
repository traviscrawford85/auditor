from typing import Literal, cast

TaskcreateFilesBodyDataPermission = Literal["private", "public"]

TASKCREATE_FILES_BODY_DATA_PERMISSION_VALUES: set[TaskcreateFilesBodyDataPermission] = {
    "private",
    "public",
}


def check_taskcreate_files_body_data_permission(value: str) -> TaskcreateFilesBodyDataPermission:
    if value in TASKCREATE_FILES_BODY_DATA_PERMISSION_VALUES:
        return cast(TaskcreateFilesBodyDataPermission, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKCREATE_FILES_BODY_DATA_PERMISSION_VALUES!r}")
