from typing import Literal, cast

TaskupdateJsonBodyDataStatus = Literal["complete", "in_progress", "in_review", "pending"]

TASKUPDATE_JSON_BODY_DATA_STATUS_VALUES: set[TaskupdateJsonBodyDataStatus] = {
    "complete",
    "in_progress",
    "in_review",
    "pending",
}


def check_taskupdate_json_body_data_status(value: str) -> TaskupdateJsonBodyDataStatus:
    if value in TASKUPDATE_JSON_BODY_DATA_STATUS_VALUES:
        return cast(TaskupdateJsonBodyDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKUPDATE_JSON_BODY_DATA_STATUS_VALUES!r}")
