from typing import Literal, cast

CalendarindexSource = Literal["mobile", "web"]

CALENDARINDEX_SOURCE_VALUES: set[CalendarindexSource] = {
    "mobile",
    "web",
}


def check_calendarindex_source(value: str) -> CalendarindexSource:
    if value in CALENDARINDEX_SOURCE_VALUES:
        return cast(CalendarindexSource, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALENDARINDEX_SOURCE_VALUES!r}")
