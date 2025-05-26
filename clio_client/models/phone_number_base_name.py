from typing import Literal, cast

PhoneNumberBaseName = Literal["Other", "Personal", "Work"]

PHONE_NUMBER_BASE_NAME_VALUES: set[PhoneNumberBaseName] = {
    "Other",
    "Personal",
    "Work",
}


def check_phone_number_base_name(value: str) -> PhoneNumberBaseName:
    if value in PHONE_NUMBER_BASE_NAME_VALUES:
        return cast(PhoneNumberBaseName, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PHONE_NUMBER_BASE_NAME_VALUES!r}")
