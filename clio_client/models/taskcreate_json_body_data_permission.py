from typing import Literal, cast

TaskcreateJsonBodyDataPermission = Literal["private", "public"]

TASKCREATE_JSON_BODY_DATA_PERMISSION_VALUES: set[TaskcreateJsonBodyDataPermission] = {
    "private",
    "public",
}


def check_taskcreate_json_body_data_permission(value: str) -> TaskcreateJsonBodyDataPermission:
    if value in TASKCREATE_JSON_BODY_DATA_PERMISSION_VALUES:
        return cast(TaskcreateJsonBodyDataPermission, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKCREATE_JSON_BODY_DATA_PERMISSION_VALUES!r}")
