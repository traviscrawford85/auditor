from typing import Literal, cast

TaskupdateJsonBodyDataPermission = Literal["private", "public"]

TASKUPDATE_JSON_BODY_DATA_PERMISSION_VALUES: set[TaskupdateJsonBodyDataPermission] = {
    "private",
    "public",
}


def check_taskupdate_json_body_data_permission(value: str) -> TaskupdateJsonBodyDataPermission:
    if value in TASKUPDATE_JSON_BODY_DATA_PERMISSION_VALUES:
        return cast(TaskupdateJsonBodyDataPermission, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKUPDATE_JSON_BODY_DATA_PERMISSION_VALUES!r}")
