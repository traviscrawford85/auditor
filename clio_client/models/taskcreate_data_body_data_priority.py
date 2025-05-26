from typing import Literal, cast

TaskcreateDataBodyDataPriority = Literal["High", "Low", "Normal"]

TASKCREATE_DATA_BODY_DATA_PRIORITY_VALUES: set[TaskcreateDataBodyDataPriority] = {
    "High",
    "Low",
    "Normal",
}


def check_taskcreate_data_body_data_priority(value: str) -> TaskcreateDataBodyDataPriority:
    if value in TASKCREATE_DATA_BODY_DATA_PRIORITY_VALUES:
        return cast(TaskcreateDataBodyDataPriority, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKCREATE_DATA_BODY_DATA_PRIORITY_VALUES!r}")
