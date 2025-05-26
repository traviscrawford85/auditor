from typing import Literal, cast

TaskTemplateListindexOrder = Literal[
    "id(asc)", "id(desc)", "name(asc)", "name(desc)", "practice_area.name(asc)", "practice_area.name(desc)"
]

TASK_TEMPLATE_LISTINDEX_ORDER_VALUES: set[TaskTemplateListindexOrder] = {
    "id(asc)",
    "id(desc)",
    "name(asc)",
    "name(desc)",
    "practice_area.name(asc)",
    "practice_area.name(desc)",
}


def check_task_template_listindex_order(value: str) -> TaskTemplateListindexOrder:
    if value in TASK_TEMPLATE_LISTINDEX_ORDER_VALUES:
        return cast(TaskTemplateListindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATE_LISTINDEX_ORDER_VALUES!r}")
