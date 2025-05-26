from typing import Literal, cast

TaskTemplateupdateDataBodyDataCascadingOffsetType = Literal[
    "BusinessDays", "CalendarDays", "CalendarMonths", "CalendarWeeks", "CalendarYears"
]

TASK_TEMPLATEUPDATE_DATA_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES: set[
    TaskTemplateupdateDataBodyDataCascadingOffsetType
] = {
    "BusinessDays",
    "CalendarDays",
    "CalendarMonths",
    "CalendarWeeks",
    "CalendarYears",
}


def check_task_templateupdate_data_body_data_cascading_offset_type(
    value: str,
) -> TaskTemplateupdateDataBodyDataCascadingOffsetType:
    if value in TASK_TEMPLATEUPDATE_DATA_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES:
        return cast(TaskTemplateupdateDataBodyDataCascadingOffsetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATEUPDATE_DATA_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES!r}"
    )
