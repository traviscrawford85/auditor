from typing import Literal, cast

TaskindexAssigneeType = Literal["contact", "user"]

TASKINDEX_ASSIGNEE_TYPE_VALUES: set[TaskindexAssigneeType] = {
    "contact",
    "user",
}


def check_taskindex_assignee_type(value: str) -> TaskindexAssigneeType:
    if value in TASKINDEX_ASSIGNEE_TYPE_VALUES:
        return cast(TaskindexAssigneeType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKINDEX_ASSIGNEE_TYPE_VALUES!r}")
