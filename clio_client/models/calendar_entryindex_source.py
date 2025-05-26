from typing import Literal, cast

CalendarEntryindexSource = Literal["mobile", "web"]

CALENDAR_ENTRYINDEX_SOURCE_VALUES: set[CalendarEntryindexSource] = {
    "mobile",
    "web",
}


def check_calendar_entryindex_source(value: str) -> CalendarEntryindexSource:
    if value in CALENDAR_ENTRYINDEX_SOURCE_VALUES:
        return cast(CalendarEntryindexSource, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALENDAR_ENTRYINDEX_SOURCE_VALUES!r}")
