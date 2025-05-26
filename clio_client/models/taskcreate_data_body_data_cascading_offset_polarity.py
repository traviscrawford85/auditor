from typing import Literal, cast

TaskcreateDataBodyDataCascadingOffsetPolarity = Literal[
    "BusinessDays", "CalendarDays", "CalendarMonths", "CalendarWeeks", "CalendarYears"
]

TASKCREATE_DATA_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES: set[TaskcreateDataBodyDataCascadingOffsetPolarity] = {
    "BusinessDays",
    "CalendarDays",
    "CalendarMonths",
    "CalendarWeeks",
    "CalendarYears",
}


def check_taskcreate_data_body_data_cascading_offset_polarity(
    value: str,
) -> TaskcreateDataBodyDataCascadingOffsetPolarity:
    if value in TASKCREATE_DATA_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES:
        return cast(TaskcreateDataBodyDataCascadingOffsetPolarity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASKCREATE_DATA_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES!r}"
    )
