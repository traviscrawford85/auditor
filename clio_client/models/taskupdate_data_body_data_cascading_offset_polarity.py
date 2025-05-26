from typing import Literal, cast

TaskupdateDataBodyDataCascadingOffsetPolarity = Literal[
    "BusinessDays", "CalendarDays", "CalendarMonths", "CalendarWeeks", "CalendarYears"
]

TASKUPDATE_DATA_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES: set[TaskupdateDataBodyDataCascadingOffsetPolarity] = {
    "BusinessDays",
    "CalendarDays",
    "CalendarMonths",
    "CalendarWeeks",
    "CalendarYears",
}


def check_taskupdate_data_body_data_cascading_offset_polarity(
    value: str,
) -> TaskupdateDataBodyDataCascadingOffsetPolarity:
    if value in TASKUPDATE_DATA_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES:
        return cast(TaskupdateDataBodyDataCascadingOffsetPolarity, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TASKUPDATE_DATA_BODY_DATA_CASCADING_OFFSET_POLARITY_VALUES!r}"
    )
