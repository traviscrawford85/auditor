from typing import Literal, cast

TaskupdateDataBodyDataAssigneeType = Literal["Contact", "User"]

TASKUPDATE_DATA_BODY_DATA_ASSIGNEE_TYPE_VALUES: set[TaskupdateDataBodyDataAssigneeType] = {
    "Contact",
    "User",
}


def check_taskupdate_data_body_data_assignee_type(value: str) -> TaskupdateDataBodyDataAssigneeType:
    if value in TASKUPDATE_DATA_BODY_DATA_ASSIGNEE_TYPE_VALUES:
        return cast(TaskupdateDataBodyDataAssigneeType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKUPDATE_DATA_BODY_DATA_ASSIGNEE_TYPE_VALUES!r}")
