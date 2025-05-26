from typing import Literal, cast

TaskTemplateindexOrder = Literal[
    "assignee.name(asc)",
    "assignee.name(desc)",
    "days_from_assignment(asc)",
    "days_from_assignment(desc)",
    "id(asc)",
    "id(desc)",
    "name(asc)",
    "name(desc)",
    "permission(asc)",
    "permission(desc)",
    "priority(asc)",
    "priority(desc)",
]

TASK_TEMPLATEINDEX_ORDER_VALUES: set[TaskTemplateindexOrder] = {
    "assignee.name(asc)",
    "assignee.name(desc)",
    "days_from_assignment(asc)",
    "days_from_assignment(desc)",
    "id(asc)",
    "id(desc)",
    "name(asc)",
    "name(desc)",
    "permission(asc)",
    "permission(desc)",
    "priority(asc)",
    "priority(desc)",
}


def check_task_templateindex_order(value: str) -> TaskTemplateindexOrder:
    if value in TASK_TEMPLATEINDEX_ORDER_VALUES:
        return cast(TaskTemplateindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATEINDEX_ORDER_VALUES!r}")
