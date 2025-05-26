from typing import Literal, cast

CalendarVisibilityBaseLightColor = Literal[
    "#00A5CA",
    "#00B177",
    "#209412",
    "#50D19B",
    "#56C4FC",
    "#5DA5C7",
    "#7BA6CD",
    "#84AB3B",
    "#959CD0",
    "#A3A2A2",
    "#B091EE",
    "#B0B0B0",
    "#BD9E69",
    "#CB5A3D",
    "#DE649D",
    "#F14A8C",
    "#F2A000",
    "#F95957",
    "#FF6B02",
    "#FF7715",
]

CALENDAR_VISIBILITY_BASE_LIGHT_COLOR_VALUES: set[CalendarVisibilityBaseLightColor] = {
    "#00A5CA",
    "#00B177",
    "#209412",
    "#50D19B",
    "#56C4FC",
    "#5DA5C7",
    "#7BA6CD",
    "#84AB3B",
    "#959CD0",
    "#A3A2A2",
    "#B091EE",
    "#B0B0B0",
    "#BD9E69",
    "#CB5A3D",
    "#DE649D",
    "#F14A8C",
    "#F2A000",
    "#F95957",
    "#FF6B02",
    "#FF7715",
}


def check_calendar_visibility_base_light_color(value: str) -> CalendarVisibilityBaseLightColor:
    if value in CALENDAR_VISIBILITY_BASE_LIGHT_COLOR_VALUES:
        return cast(CalendarVisibilityBaseLightColor, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALENDAR_VISIBILITY_BASE_LIGHT_COLOR_VALUES!r}")
