from typing import Literal, cast

CalendarEntrycreateDataBodyDataDeleted = Literal["future", "single"]

CALENDAR_ENTRYCREATE_DATA_BODY_DATA_DELETED_VALUES: set[CalendarEntrycreateDataBodyDataDeleted] = {
    "future",
    "single",
}


def check_calendar_entrycreate_data_body_data_deleted(value: str) -> CalendarEntrycreateDataBodyDataDeleted:
    if value in CALENDAR_ENTRYCREATE_DATA_BODY_DATA_DELETED_VALUES:
        return cast(CalendarEntrycreateDataBodyDataDeleted, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALENDAR_ENTRYCREATE_DATA_BODY_DATA_DELETED_VALUES!r}"
    )
