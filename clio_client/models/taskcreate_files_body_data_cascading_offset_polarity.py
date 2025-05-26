from typing import Literal, cast

TaskcreateFilesBodyDataCascadingOffsetPolarity = Literal[
    "BusinessDays", "CalendarDays", "CalendarMonths", "CalendarWeeks", "CalendarYears"
]

TASKCREATE_FILES_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES: set[TaskcreateFilesBodyDataCascadingOffsetPolarity] = {
    "BusinessDays",
    "CalendarDays",
    "CalendarMonths",
    "CalendarWeeks",
    "CalendarYears",
}


def check_taskcreate_files_body_data_cascading_offset_polarity(
    value: str,
) -> TaskcreateFilesBodyDataCascadingOffsetPolarity:
    if value in TASKCREATE_FILES_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES:
        return cast(TaskcreateFilesBodyDataCascadingOffsetPolarity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASKCREATE_FILES_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES!r}"
    )
