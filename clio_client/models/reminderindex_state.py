from typing import Literal, cast

ReminderindexState = Literal[
    "attempting_delivery",
    "delivered",
    "delivery_failed",
    "delivery_skipped",
    "initializing",
    "invalid_user",
    "rescheduling",
    "scheduled",
    "scheduling",
]

REMINDERINDEX_STATE_VALUES: set[ReminderindexState] = {
    "attempting_delivery",
    "delivered",
    "delivery_failed",
    "delivery_skipped",
    "initializing",
    "invalid_user",
    "rescheduling",
    "scheduled",
    "scheduling",
}


def check_reminderindex_state(value: str) -> ReminderindexState:
    if value in REMINDERINDEX_STATE_VALUES:
        return cast(ReminderindexState, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REMINDERINDEX_STATE_VALUES!r}")
