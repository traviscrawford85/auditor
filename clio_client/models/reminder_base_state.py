from typing import Literal, cast

ReminderBaseState = Literal[
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

REMINDER_BASE_STATE_VALUES: set[ReminderBaseState] = {
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


def check_reminder_base_state(value: str) -> ReminderBaseState:
    if value in REMINDER_BASE_STATE_VALUES:
        return cast(ReminderBaseState, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REMINDER_BASE_STATE_VALUES!r}")
