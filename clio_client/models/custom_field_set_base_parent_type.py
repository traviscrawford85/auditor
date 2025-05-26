from typing import Literal, cast

CustomFieldSetBaseParentType = Literal["Contact", "Matter"]

CUSTOM_FIELD_SET_BASE_PARENT_TYPE_VALUES: set[CustomFieldSetBaseParentType] = {
    "Contact",
    "Matter",
}


def check_custom_field_set_base_parent_type(value: str) -> CustomFieldSetBaseParentType:
    if value in CUSTOM_FIELD_SET_BASE_PARENT_TYPE_VALUES:
        return cast(CustomFieldSetBaseParentType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELD_SET_BASE_PARENT_TYPE_VALUES!r}")
