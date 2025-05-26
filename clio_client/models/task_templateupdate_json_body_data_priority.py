from typing import Literal, cast

TaskTemplateupdateJsonBodyDataPriority = Literal["High", "Low", "Normal"]

TASK_TEMPLATEUPDATE_JSON_BODY_DATA_PRIORITY_VALUES: set[TaskTemplateupdateJsonBodyDataPriority] = {
    "High",
    "Low",
    "Normal",
}


def check_task_templateupdate_json_body_data_priority(value: str) -> TaskTemplateupdateJsonBodyDataPriority:
    if value in TASK_TEMPLATEUPDATE_JSON_BODY_DATA_PRIORITY_VALUES:
        return cast(TaskTemplateupdateJsonBodyDataPriority, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATEUPDATE_JSON_BODY_DATA_PRIORITY_VALUES!r}"
    )
