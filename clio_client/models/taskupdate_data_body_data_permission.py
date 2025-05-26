from typing import Literal, cast

TaskupdateDataBodyDataPermission = Literal["private", "public"]

TASKUPDATE_DATA_BODY_DATA_PERMISSION_VALUES: set[TaskupdateDataBodyDataPermission] = {
    "private",
    "public",
}


def check_taskupdate_data_body_data_permission(value: str) -> TaskupdateDataBodyDataPermission:
    if value in TASKUPDATE_DATA_BODY_DATA_PERMISSION_VALUES:
        return cast(TaskupdateDataBodyDataPermission, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKUPDATE_DATA_BODY_DATA_PERMISSION_VALUES!r}")
