from typing import Literal, cast

ContactBaseType = Literal["Company", "Person"]

CONTACT_BASE_TYPE_VALUES: set[ContactBaseType] = {
    "Company",
    "Person",
}


def check_contact_base_type(value: str) -> ContactBaseType:
    if value in CONTACT_BASE_TYPE_VALUES:
        return cast(ContactBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_BASE_TYPE_VALUES!r}")
