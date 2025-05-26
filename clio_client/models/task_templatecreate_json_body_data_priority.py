from typing import Literal, cast

TaskTemplatecreateJsonBodyDataPriority = Literal["High", "Low", "Normal"]

TASK_TEMPLATECREATE_JSON_BODY_DATA_PRIORITY_VALUES: set[TaskTemplatecreateJsonBodyDataPriority] = {
    "High",
    "Low",
    "Normal",
}


def check_task_templatecreate_json_body_data_priority(value: str) -> TaskTemplatecreateJsonBodyDataPriority:
    if value in TASK_TEMPLATECREATE_JSON_BODY_DATA_PRIORITY_VALUES:
        return cast(TaskTemplatecreateJsonBodyDataPriority, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATECREATE_JSON_BODY_DATA_PRIORITY_VALUES!r}"
    )
