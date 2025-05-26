from typing import Literal, cast

TaskcreateFilesBodyDataCascadingOffsetType = Literal["After", "Before"]

TASKCREATE_FILES_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES: set[TaskcreateFilesBodyDataCascadingOffsetType] = {
    "After",
    "Before",
}


def check_taskcreate_files_body_data_cascading_offset_type(value: str) -> TaskcreateFilesBodyDataCascadingOffsetType:
    if value in TASKCREATE_FILES_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES:
        return cast(TaskcreateFilesBodyDataCascadingOffsetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASKCREATE_FILES_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES!r}"
    )
