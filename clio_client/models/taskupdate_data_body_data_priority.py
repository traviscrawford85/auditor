from typing import Literal, cast

TaskupdateDataBodyDataPriority = Literal["High", "Low", "Normal"]

TASKUPDATE_DATA_BODY_DATA_PRIORITY_VALUES: set[TaskupdateDataBodyDataPriority] = {
    "High",
    "Low",
    "Normal",
}


def check_taskupdate_data_body_data_priority(value: str) -> TaskupdateDataBodyDataPriority:
    if value in TASKUPDATE_DATA_BODY_DATA_PRIORITY_VALUES:
        return cast(TaskupdateDataBodyDataPriority, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKUPDATE_DATA_BODY_DATA_PRIORITY_VALUES!r}")
