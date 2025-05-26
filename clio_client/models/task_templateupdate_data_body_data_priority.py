from typing import Literal, cast

TaskTemplateupdateDataBodyDataPriority = Literal["High", "Low", "Normal"]

TASK_TEMPLATEUPDATE_DATA_BODY_DATA_PRIORITY_VALUES: set[TaskTemplateupdateDataBodyDataPriority] = {
    "High",
    "Low",
    "Normal",
}


def check_task_templateupdate_data_body_data_priority(value: str) -> TaskTemplateupdateDataBodyDataPriority:
    if value in TASK_TEMPLATEUPDATE_DATA_BODY_DATA_PRIORITY_VALUES:
        return cast(TaskTemplateupdateDataBodyDataPriority, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATEUPDATE_DATA_BODY_DATA_PRIORITY_VALUES!r}"
    )
