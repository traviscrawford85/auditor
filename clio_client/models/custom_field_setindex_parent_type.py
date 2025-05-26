from typing import Literal, cast

CustomFieldSetindexParentType = Literal["Contact", "Matter"]

CUSTOM_FIELD_SETINDEX_PARENT_TYPE_VALUES: set[CustomFieldSetindexParentType] = {
    "Contact",
    "Matter",
}


def check_custom_field_setindex_parent_type(value: str) -> CustomFieldSetindexParentType:
    if value in CUSTOM_FIELD_SETINDEX_PARENT_TYPE_VALUES:
        return cast(CustomFieldSetindexParentType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELD_SETINDEX_PARENT_TYPE_VALUES!r}")
