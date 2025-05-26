from typing import Literal, cast

AttendeeBaseType = Literal["Calendar", "Contact"]

ATTENDEE_BASE_TYPE_VALUES: set[AttendeeBaseType] = {
    "Calendar",
    "Contact",
}


def check_attendee_base_type(value: str) -> AttendeeBaseType:
    if value in ATTENDEE_BASE_TYPE_VALUES:
        return cast(AttendeeBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ATTENDEE_BASE_TYPE_VALUES!r}")
