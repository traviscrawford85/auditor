from typing import Literal, cast

CalendarVisibilityupdateFilesBodyDataColor = Literal[
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

CALENDAR_VISIBILITYUPDATE_FILES_BODY_DATA_COLOR_VALUES: set[CalendarVisibilityupdateFilesBodyDataColor] = {
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


def check_calendar_visibilityupdate_files_body_data_color(value: str) -> CalendarVisibilityupdateFilesBodyDataColor:
    if value in CALENDAR_VISIBILITYUPDATE_FILES_BODY_DATA_COLOR_VALUES:
        return cast(CalendarVisibilityupdateFilesBodyDataColor, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALENDAR_VISIBILITYUPDATE_FILES_BODY_DATA_COLOR_VALUES!r}"
    )
