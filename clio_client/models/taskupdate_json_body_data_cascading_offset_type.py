from typing import Literal, cast

TaskupdateJsonBodyDataCascadingOffsetType = Literal["After", "Before"]

TASKUPDATE_JSON_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES: set[TaskupdateJsonBodyDataCascadingOffsetType] = {
    "After",
    "Before",
}


def check_taskupdate_json_body_data_cascading_offset_type(value: str) -> TaskupdateJsonBodyDataCascadingOffsetType:
    if value in TASKUPDATE_JSON_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES:
        return cast(TaskupdateJsonBodyDataCascadingOffsetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASKUPDATE_JSON_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES!r}"
    )
