from typing import Literal, cast

TaskTemplatecreateJsonBodyDataCascadingOffsetType = Literal[
    "BusinessDays", "CalendarDays", "CalendarMonths", "CalendarWeeks", "CalendarYears"
]

TASK_TEMPLATECREATE_JSON_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES: set[
    TaskTemplatecreateJsonBodyDataCascadingOffsetType
] = {
    "BusinessDays",
    "CalendarDays",
    "CalendarMonths",
    "CalendarWeeks",
    "CalendarYears",
}


def check_task_templatecreate_json_body_data_cascading_offset_type(
    value: str,
) -> TaskTemplatecreateJsonBodyDataCascadingOffsetType:
    if value in TASK_TEMPLATECREATE_JSON_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES:
        return cast(TaskTemplatecreateJsonBodyDataCascadingOffsetType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASK_TEMPLATECREATE_JSON_BODY_DATA_CASCADING_OFFSET_TYPE_VALUES!r}"
    )
