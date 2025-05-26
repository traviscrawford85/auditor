from typing import Literal, cast

TaskupdateJsonBodyDataPriority = Literal["High", "Low", "Normal"]

TASKUPDATE_JSON_BODY_DATA_PRIORITY_VALUES: set[TaskupdateJsonBodyDataPriority] = {
    "High",
    "Low",
    "Normal",
}


def check_taskupdate_json_body_data_priority(value: str) -> TaskupdateJsonBodyDataPriority:
    if value in TASKUPDATE_JSON_BODY_DATA_PRIORITY_VALUES:
        return cast(TaskupdateJsonBodyDataPriority, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKUPDATE_JSON_BODY_DATA_PRIORITY_VALUES!r}")
