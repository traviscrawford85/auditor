from typing import Literal, cast

CalendarEntrycreateJsonBodyDataDeleted = Literal["future", "single"]

CALENDAR_ENTRYCREATE_JSON_BODY_DATA_DELETED_VALUES: set[CalendarEntrycreateJsonBodyDataDeleted] = {
    "future",
    "single",
}


def check_calendar_entrycreate_json_body_data_deleted(value: str) -> CalendarEntrycreateJsonBodyDataDeleted:
    if value in CALENDAR_ENTRYCREATE_JSON_BODY_DATA_DELETED_VALUES:
        return cast(CalendarEntrycreateJsonBodyDataDeleted, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALENDAR_ENTRYCREATE_JSON_BODY_DATA_DELETED_VALUES!r}"
    )
