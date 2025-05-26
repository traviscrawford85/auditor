from typing import Literal, cast

CustomFieldBaseParentType = Literal["Contact", "Matter"]

CUSTOM_FIELD_BASE_PARENT_TYPE_VALUES: set[CustomFieldBaseParentType] = {
    "Contact",
    "Matter",
}


def check_custom_field_base_parent_type(value: str) -> CustomFieldBaseParentType:
    if value in CUSTOM_FIELD_BASE_PARENT_TYPE_VALUES:
        return cast(CustomFieldBaseParentType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELD_BASE_PARENT_TYPE_VALUES!r}")
