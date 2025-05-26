from typing import Literal, cast

TaskTemplatecreateFilesBodyDataCascadingOffsetPolarity = Literal["After", "Before"]

TASK_TEMPLATECREATE_FILES_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES: set[
    TaskTemplatecreateFilesBodyDataCascadingOffsetPolarity
] = {
    "After",
    "Before",
}


def check_task_templatecreate_files_body_data_cascading_offset_polarity(
    value: str,
) -> TaskTemplatecreateFilesBodyDataCascadingOffsetPolarity:
    if value in TASK_TEMPLATECREATE_FILES_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES:
        return cast(TaskTemplatecreateFilesBodyDataCascadingOffsetPolarity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATECREATE_FILES_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES!r}"
    )
