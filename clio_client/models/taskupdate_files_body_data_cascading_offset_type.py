from typing import Literal, cast

TaskupdateFilesBodyDataCascadingOffsetType = Literal["After", "Before"]

TASKUPDATE_FILES_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES: set[TaskupdateFilesBodyDataCascadingOffsetType] = {
    "After",
    "Before",
}


def check_taskupdate_files_body_data_cascading_offset_type(value: str) -> TaskupdateFilesBodyDataCascadingOffsetType:
    if value in TASKUPDATE_FILES_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES:
        return cast(TaskupdateFilesBodyDataCascadingOffsetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASKUPDATE_FILES_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES!r}"
    )
