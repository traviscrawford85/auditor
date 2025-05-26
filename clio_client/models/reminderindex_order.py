from typing import Literal, cast

ReminderindexOrder = Literal["id(asc)", "id(desc)", "next_delivery_at(asc)", "next_delivery_at(desc)"]

REMINDERINDEX_ORDER_VALUES: set[ReminderindexOrder] = {
    "id(asc)",
    "id(desc)",
    "next_delivery_at(asc)",
    "next_delivery_at(desc)",
}


def check_reminderindex_order(value: str) -> ReminderindexOrder:
    if value in REMINDERINDEX_ORDER_VALUES:
        return cast(ReminderindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REMINDERINDEX_ORDER_VALUES!r}")
