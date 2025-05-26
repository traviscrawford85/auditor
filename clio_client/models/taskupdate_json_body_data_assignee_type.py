from typing import Literal, cast

TaskupdateJsonBodyDataAssigneeType = Literal["Contact", "User"]

TASKUPDATE_JSON_BODY_DATA_ASSIGNEE_TYPE_VALUES: set[TaskupdateJsonBodyDataAssigneeType] = {
    "Contact",
    "User",
}


def check_taskupdate_json_body_data_assignee_type(value: str) -> TaskupdateJsonBodyDataAssigneeType:
    if value in TASKUPDATE_JSON_BODY_DATA_ASSIGNEE_TYPE_VALUES:
        return cast(TaskupdateJsonBodyDataAssigneeType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKUPDATE_JSON_BODY_DATA_ASSIGNEE_TYPE_VALUES!r}")
