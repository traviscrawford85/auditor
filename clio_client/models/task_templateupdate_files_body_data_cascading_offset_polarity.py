from typing import Literal, cast

TaskTemplateupdateFilesBodyDataCascadingOffsetPolarity = Literal["After", "Before"]

TASK_TEMPLATEUPDATE_FILES_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES: set[
    TaskTemplateupdateFilesBodyDataCascadingOffsetPolarity
] = {
    "After",
    "Before",
}


def check_task_templateupdate_files_body_data_cascading_offset_polarity(
    value: str,
) -> TaskTemplateupdateFilesBodyDataCascadingOffsetPolarity:
    if value in TASK_TEMPLATEUPDATE_FILES_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES:
        return cast(TaskTemplateupdateFilesBodyDataCascadingOffsetPolarity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATEUPDATE_FILES_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES!r}"
    )
