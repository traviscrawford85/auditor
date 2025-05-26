from typing import Literal, cast

TaskupdateDataBodyDataStatus = Literal["complete", "in_progress", "in_review", "pending"]

TASKUPDATE_DATA_BODY_DATA_STATUS_VALUES: set[TaskupdateDataBodyDataStatus] = {
    "complete",
    "in_progress",
    "in_review",
    "pending",
}


def check_taskupdate_data_body_data_status(value: str) -> TaskupdateDataBodyDataStatus:
    if value in TASKUPDATE_DATA_BODY_DATA_STATUS_VALUES:
        return cast(TaskupdateDataBodyDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKUPDATE_DATA_BODY_DATA_STATUS_VALUES!r}")
