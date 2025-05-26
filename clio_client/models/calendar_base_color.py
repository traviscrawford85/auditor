from typing import Literal, cast

CalendarBaseColor = Literal[
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

CALENDAR_BASE_COLOR_VALUES: set[CalendarBaseColor] = {
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


def check_calendar_base_color(value: str) -> CalendarBaseColor:
    if value in CALENDAR_BASE_COLOR_VALUES:
        return cast(CalendarBaseColor, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALENDAR_BASE_COLOR_VALUES!r}")
