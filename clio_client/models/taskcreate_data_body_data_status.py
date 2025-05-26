from typing import Literal, cast

TaskcreateDataBodyDataStatus = Literal["complete", "in_progress", "in_review", "pending"]

TASKCREATE_DATA_BODY_DATA_STATUS_VALUES: set[TaskcreateDataBodyDataStatus] = {
    "complete",
    "in_progress",
    "in_review",
    "pending",
}


def check_taskcreate_data_body_data_status(value: str) -> TaskcreateDataBodyDataStatus:
    if value in TASKCREATE_DATA_BODY_DATA_STATUS_VALUES:
        return cast(TaskcreateDataBodyDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKCREATE_DATA_BODY_DATA_STATUS_VALUES!r}")
