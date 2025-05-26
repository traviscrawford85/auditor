from typing import Literal, cast

TaskcreateJsonBodyDataCascadingOffsetType = Literal["After", "Before"]

TASKCREATE_JSON_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES: set[TaskcreateJsonBodyDataCascadingOffsetType] = {
    "After",
    "Before",
}


def check_taskcreate_json_body_data_cascading_offset_type(value: str) -> TaskcreateJsonBodyDataCascadingOffsetType:
    if value in TASKCREATE_JSON_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES:
        return cast(TaskcreateJsonBodyDataCascadingOffsetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASKCREATE_JSON_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES!r}"
    )
