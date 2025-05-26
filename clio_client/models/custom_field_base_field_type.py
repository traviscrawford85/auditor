from typing import Literal, cast

CustomFieldBaseFieldType = Literal[
    "checkbox",
    "contact",
    "currency",
    "date",
    "email",
    "matter",
    "numeric",
    "picklist",
    "text_area",
    "text_line",
    "time",
    "url",
]

CUSTOM_FIELD_BASE_FIELD_TYPE_VALUES: set[CustomFieldBaseFieldType] = {
    "checkbox",
    "contact",
    "currency",
    "date",
    "email",
    "matter",
    "numeric",
    "picklist",
    "text_area",
    "text_line",
    "time",
    "url",
}


def check_custom_field_base_field_type(value: str) -> CustomFieldBaseFieldType:
    if value in CUSTOM_FIELD_BASE_FIELD_TYPE_VALUES:
        return cast(CustomFieldBaseFieldType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELD_BASE_FIELD_TYPE_VALUES!r}")
