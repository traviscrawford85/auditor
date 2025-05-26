from typing import Literal, cast

RelatedContactsBaseType = Literal["Company", "Person"]

RELATED_CONTACTS_BASE_TYPE_VALUES: set[RelatedContactsBaseType] = {
    "Company",
    "Person",
}


def check_related_contacts_base_type(value: str) -> RelatedContactsBaseType:
    if value in RELATED_CONTACTS_BASE_TYPE_VALUES:
        return cast(RelatedContactsBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RELATED_CONTACTS_BASE_TYPE_VALUES!r}")
