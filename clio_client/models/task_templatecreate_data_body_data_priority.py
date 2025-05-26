from typing import Literal, cast

TaskTemplatecreateDataBodyDataPriority = Literal["High", "Low", "Normal"]

TASK_TEMPLATECREATE_DATA_BODY_DATA_PRIORITY_VALUES: set[TaskTemplatecreateDataBodyDataPriority] = {
    "High",
    "Low",
    "Normal",
}


def check_task_templatecreate_data_body_data_priority(value: str) -> TaskTemplatecreateDataBodyDataPriority:
    if value in TASK_TEMPLATECREATE_DATA_BODY_DATA_PRIORITY_VALUES:
        return cast(TaskTemplatecreateDataBodyDataPriority, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATECREATE_DATA_BODY_DATA_PRIORITY_VALUES!r}"
    )
