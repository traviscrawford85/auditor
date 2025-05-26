from typing import Literal, cast

TaskcreateDataBodyDataPermission = Literal["private", "public"]

TASKCREATE_DATA_BODY_DATA_PERMISSION_VALUES: set[TaskcreateDataBodyDataPermission] = {
    "private",
    "public",
}


def check_taskcreate_data_body_data_permission(value: str) -> TaskcreateDataBodyDataPermission:
    if value in TASKCREATE_DATA_BODY_DATA_PERMISSION_VALUES:
        return cast(TaskcreateDataBodyDataPermission, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKCREATE_DATA_BODY_DATA_PERMISSION_VALUES!r}")
