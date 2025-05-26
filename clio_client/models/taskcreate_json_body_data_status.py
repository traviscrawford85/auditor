from typing import Literal, cast

TaskcreateJsonBodyDataStatus = Literal["complete", "in_progress", "in_review", "pending"]

TASKCREATE_JSON_BODY_DATA_STATUS_VALUES: set[TaskcreateJsonBodyDataStatus] = {
    "complete",
    "in_progress",
    "in_review",
    "pending",
}


def check_taskcreate_json_body_data_status(value: str) -> TaskcreateJsonBodyDataStatus:
    if value in TASKCREATE_JSON_BODY_DATA_STATUS_VALUES:
        return cast(TaskcreateJsonBodyDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TASKCREATE_JSON_BODY_DATA_STATUS_VALUES!r}")
