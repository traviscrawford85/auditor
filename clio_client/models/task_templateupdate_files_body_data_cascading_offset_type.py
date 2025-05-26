from typing import Literal, cast

TaskTemplateupdateFilesBodyDataCascadingOffsetType = Literal[
    "BusinessDays", "CalendarDays", "CalendarMonths", "CalendarWeeks", "CalendarYears"
]

TASK_TEMPLATEUPDATE_FILES_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES: set[
    TaskTemplateupdateFilesBodyDataCascadingOffsetType
] = {
    "BusinessDays",
    "CalendarDays",
    "CalendarMonths",
    "CalendarWeeks",
    "CalendarYears",
}


def check_task_templateupdate_files_body_data_cascading_offset_type(
    value: str,
) -> TaskTemplateupdateFilesBodyDataCascadingOffsetType:
    if value in TASK_TEMPLATEUPDATE_FILES_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES:
        return cast(TaskTemplateupdateFilesBodyDataCascadingOffsetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATEUPDATE_FILES_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES!r}"
    )
