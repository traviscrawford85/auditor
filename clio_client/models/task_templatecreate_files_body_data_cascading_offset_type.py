from typing import Literal, cast

TaskTemplatecreateFilesBodyDataCascadingOffsetType = Literal[
    "BusinessDays", "CalendarDays", "CalendarMonths", "CalendarWeeks", "CalendarYears"
]

TASK_TEMPLATECREATE_FILES_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES: set[
    TaskTemplatecreateFilesBodyDataCascadingOffsetType
] = {
    "BusinessDays",
    "CalendarDays",
    "CalendarMonths",
    "CalendarWeeks",
    "CalendarYears",
}


def check_task_templatecreate_files_body_data_cascading_offset_type(
    value: str,
) -> TaskTemplatecreateFilesBodyDataCascadingOffsetType:
    if value in TASK_TEMPLATECREATE_FILES_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES:
        return cast(TaskTemplatecreateFilesBodyDataCascadingOffsetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATECREATE_FILES_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES!r}"
    )
