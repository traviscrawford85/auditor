from typing import Literal, cast

TaskindexStatus = Literal["complete", "in_progress", "in_review", "pending"]

TASKINDEX_STATUS_VALUES: set[TaskindexStatus] = {
    "complete",
    "in_progress",
    "in_review",
    "pending",
}


def check_taskindex_status(value: str) -> TaskindexStatus:
    if value in TASKINDEX_STATUS_VALUES:
        return cast(TaskindexStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKINDEX_STATUS_VALUES!r}")
