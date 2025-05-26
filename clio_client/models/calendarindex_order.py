from typing import Literal, cast

CalendarindexOrder = Literal["id(asc)", "id(desc)", "name(asc)", "name(desc)"]

CALENDARINDEX_ORDER_VALUES: set[CalendarindexOrder] = {
    "id(asc)",
    "id(desc)",
    "name(asc)",
    "name(desc)",
}


def check_calendarindex_order(value: str) -> CalendarindexOrder:
    if value in CALENDARINDEX_ORDER_VALUES:
        return cast(CalendarindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALENDARINDEX_ORDER_VALUES!r}")
