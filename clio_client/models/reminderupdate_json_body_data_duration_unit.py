from typing import Literal, cast

ReminderupdateJsonBodyDataDurationUnit = Literal["days", "hours", "minutes", "weeks"]

REMINDERUPDATE_JSON_BODY_DATA_DURATION_UNIT_VALUES: set[ReminderupdateJsonBodyDataDurationUnit] = {
    "days",
    "hours",
    "minutes",
    "weeks",
}


def check_reminderupdate_json_body_data_duration_unit(value: str) -> ReminderupdateJsonBodyDataDurationUnit:
    if value in REMINDERUPDATE_JSON_BODY_DATA_DURATION_UNIT_VALUES:
        return cast(ReminderupdateJsonBodyDataDurationUnit, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMINDERUPDATE_JSON_BODY_DATA_DURATION_UNIT_VALUES!r}"
    )
