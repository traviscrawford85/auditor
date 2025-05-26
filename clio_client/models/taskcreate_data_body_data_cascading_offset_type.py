from typing import Literal, cast

TaskcreateDataBodyDataCascadingOffsetType = Literal["After", "Before"]

TASKCREATE_DATA_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES: set[TaskcreateDataBodyDataCascadingOffsetType] = {
    "After",
    "Before",
}


def check_taskcreate_data_body_data_cascading_offset_type(value: str) -> TaskcreateDataBodyDataCascadingOffsetType:
    if value in TASKCREATE_DATA_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES:
        return cast(TaskcreateDataBodyDataCascadingOffsetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASKCREATE_DATA_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES!r}"
    )
