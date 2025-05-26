from typing import Literal, cast

ReminderupdateDataBodyDataDurationUnit = Literal["days", "hours", "minutes", "weeks"]

REMINDERUPDATE_DATA_BODY_DATA_DURATION_UNIT_VALUES: set[ReminderupdateDataBodyDataDurationUnit] = {
    "days",
    "hours",
    "minutes",
    "weeks",
}


def check_reminderupdate_data_body_data_duration_unit(value: str) -> ReminderupdateDataBodyDataDurationUnit:
    if value in REMINDERUPDATE_DATA_BODY_DATA_DURATION_UNIT_VALUES:
        return cast(ReminderupdateDataBodyDataDurationUnit, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMINDERUPDATE_DATA_BODY_DATA_DURATION_UNIT_VALUES!r}"
    )
