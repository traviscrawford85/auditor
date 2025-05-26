from typing import Literal, cast

TaskupdateJsonBodyDataCascadingOffsetPolarity = Literal[
    "BusinessDays", "CalendarDays", "CalendarMonths", "CalendarWeeks", "CalendarYears"
]

TASKUPDATE_JSON_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES: set[TaskupdateJsonBodyDataCascadingOffsetPolarity] = {
    "BusinessDays",
    "CalendarDays",
    "CalendarMonths",
    "CalendarWeeks",
    "CalendarYears",
}


def check_taskupdate_json_body_data_cascading_offset_polarity(
    value: str,
) -> TaskupdateJsonBodyDataCascadingOffsetPolarity:
    if value in TASKUPDATE_JSON_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES:
        return cast(TaskupdateJsonBodyDataCascadingOffsetPolarity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASKUPDATE_JSON_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES!r}"
    )
