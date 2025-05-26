from typing import Literal, cast

TaskTypeindexOrder = Literal["id(asc)", "id(desc)", "name(asc)", "name(desc)"]

TASK_TYPEINDEX_ORDER_VALUES: set[TaskTypeindexOrder] = {
    "id(asc)",
    "id(desc)",
    "name(asc)",
    "name(desc)",
}


def check_task_typeindex_order(value: str) -> TaskTypeindexOrder:
    if value in TASK_TYPEINDEX_ORDER_VALUES:
        return cast(TaskTypeindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASK_TYPEINDEX_ORDER_VALUES!r}")
