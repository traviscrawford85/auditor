from typing import Literal, cast

TaskindexOrder = Literal[
    "completed_at(asc)",
    "completed_at(desc)",
    "due_at(asc)",
    "due_at(desc)",
    "due_at_strict(asc)",
    "due_at_strict(desc)",
    "id(asc)",
    "id(desc)",
    "matter.display_number(asc)",
    "matter.display_number(desc)",
    "name(asc)",
    "name(desc)",
    "priority(asc)",
    "priority(desc)",
    "task_type.name(asc)",
    "task_type.name(desc)",
]

TASKINDEX_ORDER_VALUES: set[TaskindexOrder] = {
    "completed_at(asc)",
    "completed_at(desc)",
    "due_at(asc)",
    "due_at(desc)",
    "due_at_strict(asc)",
    "due_at_strict(desc)",
    "id(asc)",
    "id(desc)",
    "matter.display_number(asc)",
    "matter.display_number(desc)",
    "name(asc)",
    "name(desc)",
    "priority(asc)",
    "priority(desc)",
    "task_type.name(asc)",
    "task_type.name(desc)",
}


def check_taskindex_order(value: str) -> TaskindexOrder:
    if value in TASKINDEX_ORDER_VALUES:
        return cast(TaskindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKINDEX_ORDER_VALUES!r}")
