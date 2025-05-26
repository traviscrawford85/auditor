from typing import Literal, cast

TaskupdateFilesBodyDataCascadingOffsetPolarity = Literal[
    "BusinessDays", "CalendarDays", "CalendarMonths", "CalendarWeeks", "CalendarYears"
]

TASKUPDATE_FILES_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES: set[TaskupdateFilesBodyDataCascadingOffsetPolarity] = {
    "BusinessDays",
    "CalendarDays",
    "CalendarMonths",
    "CalendarWeeks",
    "CalendarYears",
}


def check_taskupdate_files_body_data_cascading_offset_polarity(
    value: str,
) -> TaskupdateFilesBodyDataCascadingOffsetPolarity:
    if value in TASKUPDATE_FILES_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES:
        return cast(TaskupdateFilesBodyDataCascadingOffsetPolarity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASKUPDATE_FILES_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES!r}"
    )
