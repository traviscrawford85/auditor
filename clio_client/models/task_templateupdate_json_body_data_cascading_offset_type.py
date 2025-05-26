from typing import Literal, cast

TaskTemplateupdateJsonBodyDataCascadingOffsetType = Literal[
    "BusinessDays", "CalendarDays", "CalendarMonths", "CalendarWeeks", "CalendarYears"
]

TASK_TEMPLATEUPDATE_JSON_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES: set[
    TaskTemplateupdateJsonBodyDataCascadingOffsetType
] = {
    "BusinessDays",
    "CalendarDays",
    "CalendarMonths",
    "CalendarWeeks",
    "CalendarYears",
}


def check_task_templateupdate_json_body_data_cascading_offset_type(
    value: str,
) -> TaskTemplateupdateJsonBodyDataCascadingOffsetType:
    if value in TASK_TEMPLATEUPDATE_JSON_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES:
        return cast(TaskTemplateupdateJsonBodyDataCascadingOffsetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATEUPDATE_JSON_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES!r}"
    )
