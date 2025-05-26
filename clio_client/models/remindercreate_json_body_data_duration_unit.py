from typing import Literal, cast

RemindercreateJsonBodyDataDurationUnit = Literal["days", "hours", "minutes", "weeks"]

REMINDERCREATE_JSON_BODY_DATA_DURATION_UNIT_VALUES: set[RemindercreateJsonBodyDataDurationUnit] = {
    "days",
    "hours",
    "minutes",
    "weeks",
}


def check_remindercreate_json_body_data_duration_unit(value: str) -> RemindercreateJsonBodyDataDurationUnit:
    if value in REMINDERCREATE_JSON_BODY_DATA_DURATION_UNIT_VALUES:
        return cast(RemindercreateJsonBodyDataDurationUnit, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMINDERCREATE_JSON_BODY_DATA_DURATION_UNIT_VALUES!r}"
    )
