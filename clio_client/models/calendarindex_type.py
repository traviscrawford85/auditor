from typing import Literal, cast

CalendarindexType = Literal["AccountCalendar", "AdhocCalendar", "UserCalendar"]

CALENDARINDEX_TYPE_VALUES: set[CalendarindexType] = {
    "AccountCalendar",
    "AdhocCalendar",
    "UserCalendar",
}


def check_calendarindex_type(value: str) -> CalendarindexType:
    if value in CALENDARINDEX_TYPE_VALUES:
        return cast(CalendarindexType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALENDARINDEX_TYPE_VALUES!r}")
