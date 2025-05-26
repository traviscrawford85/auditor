from typing import Literal, cast

TaskcreateJsonBodyDataAssigneeType = Literal["Contact", "User"]

TASKCREATE_JSON_BODY_DATA_ASSIGNEE_TYPE_VALUES: set[TaskcreateJsonBodyDataAssigneeType] = {
    "Contact",
    "User",
}


def check_taskcreate_json_body_data_assignee_type(value: str) -> TaskcreateJsonBodyDataAssigneeType:
    if value in TASKCREATE_JSON_BODY_DATA_ASSIGNEE_TYPE_VALUES:
        return cast(TaskcreateJsonBodyDataAssigneeType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKCREATE_JSON_BODY_DATA_ASSIGNEE_TYPE_VALUES!r}")
