from typing import Literal, cast

RemindercreateDataBodyDataDurationUnit = Literal["days", "hours", "minutes", "weeks"]

REMINDERCREATE_DATA_BODY_DATA_DURATION_UNIT_VALUES: set[RemindercreateDataBodyDataDurationUnit] = {
    "days",
    "hours",
    "minutes",
    "weeks",
}


def check_remindercreate_data_body_data_duration_unit(value: str) -> RemindercreateDataBodyDataDurationUnit:
    if value in REMINDERCREATE_DATA_BODY_DATA_DURATION_UNIT_VALUES:
        return cast(RemindercreateDataBodyDataDurationUnit, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMINDERCREATE_DATA_BODY_DATA_DURATION_UNIT_VALUES!r}"
    )
