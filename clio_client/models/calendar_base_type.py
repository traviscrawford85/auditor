from typing import Literal, cast

CalendarBaseType = Literal["AccountCalendar", "AdhocCalendar", "UserCalendar"]

CALENDAR_BASE_TYPE_VALUES: set[CalendarBaseType] = {
    "AccountCalendar",
    "AdhocCalendar",
    "UserCalendar",
}


def check_calendar_base_type(value: str) -> CalendarBaseType:
    if value in CALENDAR_BASE_TYPE_VALUES:
        return cast(CalendarBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALENDAR_BASE_TYPE_VALUES!r}")
