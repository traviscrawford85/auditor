from typing import Literal, cast

TaskcreateDataBodyDataAssigneeType = Literal["Contact", "User"]

TASKCREATE_DATA_BODY_DATA_ASSIGNEE_TYPE_VALUES: set[TaskcreateDataBodyDataAssigneeType] = {
    "Contact",
    "User",
}


def check_taskcreate_data_body_data_assignee_type(value: str) -> TaskcreateDataBodyDataAssigneeType:
    if value in TASKCREATE_DATA_BODY_DATA_ASSIGNEE_TYPE_VALUES:
        return cast(TaskcreateDataBodyDataAssigneeType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKCREATE_DATA_BODY_DATA_ASSIGNEE_TYPE_VALUES!r}")
