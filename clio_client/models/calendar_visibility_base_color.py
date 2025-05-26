from typing import Literal, cast

CalendarVisibilityBaseColor = Literal[
    "#49B050",
    "#56BFB3",
    "#64AD88",
    "#658CB3",
    "#658CDA",
    "#84AAA5",
    "#8897A5",
    "#8BBF3C",
    "#8C66DA",
    "#93A2BE",
    "#A7A77D",
    "#A992A9",
    "#B473B4",
    "#BE9494",
    "#BFBF4B",
    "#C4A882",
    "#DA6666",
    "#E77399",
    "#E7804C",
    "#F2A53D",
]

CALENDAR_VISIBILITY_BASE_COLOR_VALUES: set[CalendarVisibilityBaseColor] = {
    "#49B050",
    "#56BFB3",
    "#64AD88",
    "#658CB3",
    "#658CDA",
    "#84AAA5",
    "#8897A5",
    "#8BBF3C",
    "#8C66DA",
    "#93A2BE",
    "#A7A77D",
    "#A992A9",
    "#B473B4",
    "#BE9494",
    "#BFBF4B",
    "#C4A882",
    "#DA6666",
    "#E77399",
    "#E7804C",
    "#F2A53D",
}


def check_calendar_visibility_base_color(value: str) -> CalendarVisibilityBaseColor:
    if value in CALENDAR_VISIBILITY_BASE_COLOR_VALUES:
        return cast(CalendarVisibilityBaseColor, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALENDAR_VISIBILITY_BASE_COLOR_VALUES!r}")
