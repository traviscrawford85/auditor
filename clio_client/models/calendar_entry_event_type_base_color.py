from typing import Literal, cast

CalendarEntryEventTypeBaseColor = Literal[
    "#009CEC",
    "#367B9C",
    "#616161",
    "#62D6B1",
    "#6AC9DE",
    "#83D17F",
    "#8E3F64",
    "#9EEDCB",
    "#BBDA81",
    "#BFC2E1",
    "#C75300",
    "#CDE2F5",
    "#D6C4A5",
    "#DADADA",
    "#DFD3F8",
    "#EABBB0",
    "#F9A2C4",
    "#FFA5A4",
    "#FFAC7B",
    "#FFD478",
]

CALENDAR_ENTRY_EVENT_TYPE_BASE_COLOR_VALUES: set[CalendarEntryEventTypeBaseColor] = {
    "#009CEC",
    "#367B9C",
    "#616161",
    "#62D6B1",
    "#6AC9DE",
    "#83D17F",
    "#8E3F64",
    "#9EEDCB",
    "#BBDA81",
    "#BFC2E1",
    "#C75300",
    "#CDE2F5",
    "#D6C4A5",
    "#DADADA",
    "#DFD3F8",
    "#EABBB0",
    "#F9A2C4",
    "#FFA5A4",
    "#FFAC7B",
    "#FFD478",
}


def check_calendar_entry_event_type_base_color(value: str) -> CalendarEntryEventTypeBaseColor:
    if value in CALENDAR_ENTRY_EVENT_TYPE_BASE_COLOR_VALUES:
        return cast(CalendarEntryEventTypeBaseColor, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALENDAR_ENTRY_EVENT_TYPE_BASE_COLOR_VALUES!r}")
