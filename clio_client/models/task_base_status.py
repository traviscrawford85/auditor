from typing import Literal, cast

TaskBaseStatus = Literal["complete", "in_progress", "in_review", "pending"]

TASK_BASE_STATUS_VALUES: set[TaskBaseStatus] = {
    "complete",
    "in_progress",
    "in_review",
    "pending",
}


def check_task_base_status(value: str) -> TaskBaseStatus:
    if value in TASK_BASE_STATUS_VALUES:
        return cast(TaskBaseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASK_BASE_STATUS_VALUES!r}")
