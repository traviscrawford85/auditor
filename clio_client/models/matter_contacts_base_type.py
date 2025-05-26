from typing import Literal, cast

MatterContactsBaseType = Literal["Company", "Person"]

MATTER_CONTACTS_BASE_TYPE_VALUES: set[MatterContactsBaseType] = {
    "Company",
    "Person",
}


def check_matter_contacts_base_type(value: str) -> MatterContactsBaseType:
    if value in MATTER_CONTACTS_BASE_TYPE_VALUES:
        return cast(MatterContactsBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATTER_CONTACTS_BASE_TYPE_VALUES!r}")
