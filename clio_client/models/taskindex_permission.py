from typing import Literal, cast

TaskindexPermission = Literal["private", "public"]

TASKINDEX_PERMISSION_VALUES: set[TaskindexPermission] = {
    "private",
    "public",
}


def check_taskindex_permission(value: str) -> TaskindexPermission:
    if value in TASKINDEX_PERMISSION_VALUES:
        return cast(TaskindexPermission, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKINDEX_PERMISSION_VALUES!r}")
