from typing import Literal, cast

TaskindexPriority = Literal["high", "low", "normal"]

TASKINDEX_PRIORITY_VALUES: set[TaskindexPriority] = {
    "high",
    "low",
    "normal",
}


def check_taskindex_priority(value: str) -> TaskindexPriority:
    if value in TASKINDEX_PRIORITY_VALUES:
        return cast(TaskindexPriority, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKINDEX_PRIORITY_VALUES!r}")
