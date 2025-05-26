from typing import Literal, cast

TaskBasePriority = Literal["High", "Low", "Normal"]

TASK_BASE_PRIORITY_VALUES: set[TaskBasePriority] = {
    "High",
    "Low",
    "Normal",
}


def check_task_base_priority(value: str) -> TaskBasePriority:
    if value in TASK_BASE_PRIORITY_VALUES:
        return cast(TaskBasePriority, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASK_BASE_PRIORITY_VALUES!r}")
