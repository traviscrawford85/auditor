from typing import Literal, cast

InstantMessengerBaseName = Literal["Other", "Personal", "Work"]

INSTANT_MESSENGER_BASE_NAME_VALUES: set[InstantMessengerBaseName] = {
    "Other",
    "Personal",
    "Work",
}


def check_instant_messenger_base_name(value: str) -> InstantMessengerBaseName:
    if value in INSTANT_MESSENGER_BASE_NAME_VALUES:
        return cast(InstantMessengerBaseName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INSTANT_MESSENGER_BASE_NAME_VALUES!r}")
