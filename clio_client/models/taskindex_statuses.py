from typing import Literal, cast

TaskindexStatuses = Literal["complete", "in_progress", "in_review", "pending"]

TASKINDEX_STATUSES_VALUES: set[TaskindexStatuses] = {
    "complete",
    "in_progress",
    "in_review",
    "pending",
}


def check_taskindex_statuses(value: str) -> TaskindexStatuses:
    if value in TASKINDEX_STATUSES_VALUES:
        return cast(TaskindexStatuses, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKINDEX_STATUSES_VALUES!r}")
