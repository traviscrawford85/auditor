from typing import Literal, cast

CustomFieldindexParentType = Literal["contact", "matter"]

CUSTOM_FIELDINDEX_PARENT_TYPE_VALUES: set[CustomFieldindexParentType] = {
    "contact",
    "matter",
}


def check_custom_fieldindex_parent_type(value: str) -> CustomFieldindexParentType:
    if value in CUSTOM_FIELDINDEX_PARENT_TYPE_VALUES:
        return cast(CustomFieldindexParentType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELDINDEX_PARENT_TYPE_VALUES!r}")
