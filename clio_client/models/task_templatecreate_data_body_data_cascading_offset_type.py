from typing import Literal, cast

TaskTemplatecreateDataBodyDataCascadingOffsetType = Literal[
    "BusinessDays", "CalendarDays", "CalendarMonths", "CalendarWeeks", "CalendarYears"
]

TASK_TEMPLATECREATE_DATA_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES: set[
    TaskTemplatecreateDataBodyDataCascadingOffsetType
] = {
    "BusinessDays",
    "CalendarDays",
    "CalendarMonths",
    "CalendarWeeks",
    "CalendarYears",
}


def check_task_templatecreate_data_body_data_cascading_offset_type(
    value: str,
) -> TaskTemplatecreateDataBodyDataCascadingOffsetType:
    if value in TASK_TEMPLATECREATE_DATA_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES:
        return cast(TaskTemplatecreateDataBodyDataCascadingOffsetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATECREATE_DATA_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES!r}"
    )
