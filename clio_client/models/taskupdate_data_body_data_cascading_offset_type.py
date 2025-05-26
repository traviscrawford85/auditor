from typing import Literal, cast

TaskupdateDataBodyDataCascadingOffsetType = Literal["After", "Before"]

TASKUPDATE_DATA_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES: set[TaskupdateDataBodyDataCascadingOffsetType] = {
    "After",
    "Before",
}


def check_taskupdate_data_body_data_cascading_offset_type(value: str) -> TaskupdateDataBodyDataCascadingOffsetType:
    if value in TASKUPDATE_DATA_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES:
        return cast(TaskupdateDataBodyDataCascadingOffsetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASKUPDATE_DATA_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES!r}"
    )
