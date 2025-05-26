from typing import Literal, cast

CalendarBaseSource = Literal["mobile", "web"]

CALENDAR_BASE_SOURCE_VALUES: set[CalendarBaseSource] = {
    "mobile",
    "web",
}


def check_calendar_base_source(value: str) -> CalendarBaseSource:
    if value in CALENDAR_BASE_SOURCE_VALUES:
        return cast(CalendarBaseSource, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALENDAR_BASE_SOURCE_VALUES!r}")
