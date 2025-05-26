from typing import Literal, cast

TaskTemplateBasePriority = Literal["High", "Low", "Normal"]

TASK_TEMPLATE_BASE_PRIORITY_VALUES: set[TaskTemplateBasePriority] = {
    "High",
    "Low",
    "Normal",
}


def check_task_template_base_priority(value: str) -> TaskTemplateBasePriority:
    if value in TASK_TEMPLATE_BASE_PRIORITY_VALUES:
        return cast(TaskTemplateBasePriority, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATE_BASE_PRIORITY_VALUES!r}")
