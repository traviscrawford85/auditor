from typing import Literal, cast

CalendarBasePermission = Literal["editor", "limited_viewer", "none", "owner", "viewer"]

CALENDAR_BASE_PERMISSION_VALUES: set[CalendarBasePermission] = {
    "editor",
    "limited_viewer",
    "none",
    "owner",
    "viewer",
}


def check_calendar_base_permission(value: str) -> CalendarBasePermission:
    if value in CALENDAR_BASE_PERMISSION_VALUES:
        return cast(CalendarBasePermission, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALENDAR_BASE_PERMISSION_VALUES!r}")
