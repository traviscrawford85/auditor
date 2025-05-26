from typing import Literal, cast

TaskcreateJsonBodyDataPriority = Literal["High", "Low", "Normal"]

TASKCREATE_JSON_BODY_DATA_PRIORITY_VALUES: set[TaskcreateJsonBodyDataPriority] = {
    "High",
    "Low",
    "Normal",
}


def check_taskcreate_json_body_data_priority(value: str) -> TaskcreateJsonBodyDataPriority:
    if value in TASKCREATE_JSON_BODY_DATA_PRIORITY_VALUES:
        return cast(TaskcreateJsonBodyDataPriority, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKCREATE_JSON_BODY_DATA_PRIORITY_VALUES!r}")
