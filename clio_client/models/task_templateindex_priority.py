from typing import Literal, cast

TaskTemplateindexPriority = Literal["high", "low", "normal"]

TASK_TEMPLATEINDEX_PRIORITY_VALUES: set[TaskTemplateindexPriority] = {
    "high",
    "low",
    "normal",
}


def check_task_templateindex_priority(value: str) -> TaskTemplateindexPriority:
    if value in TASK_TEMPLATEINDEX_PRIORITY_VALUES:
        return cast(TaskTemplateindexPriority, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATEINDEX_PRIORITY_VALUES!r}")
