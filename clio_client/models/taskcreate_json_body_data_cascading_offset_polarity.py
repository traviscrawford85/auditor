from typing import Literal, cast

TaskcreateJsonBodyDataCascadingOffsetPolarity = Literal[
    "BusinessDays", "CalendarDays", "CalendarMonths", "CalendarWeeks", "CalendarYears"
]

TASKCREATE_JSON_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES: set[TaskcreateJsonBodyDataCascadingOffsetPolarity] = {
    "BusinessDays",
    "CalendarDays",
    "CalendarMonths",
    "CalendarWeeks",
    "CalendarYears",
}


def check_taskcreate_json_body_data_cascading_offset_polarity(
    value: str,
) -> TaskcreateJsonBodyDataCascadingOffsetPolarity:
    if value in TASKCREATE_JSON_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES:
        return cast(TaskcreateJsonBodyDataCascadingOffsetPolarity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASKCREATE_JSON_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES!r}"
    )
