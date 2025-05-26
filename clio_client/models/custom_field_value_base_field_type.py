from typing import Literal, cast

CustomFieldValueBaseFieldType = Literal[
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

CUSTOM_FIELD_VALUE_BASE_FIELD_TYPE_VALUES: set[CustomFieldValueBaseFieldType] = {
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


def check_custom_field_value_base_field_type(value: str) -> CustomFieldValueBaseFieldType:
    if value in CUSTOM_FIELD_VALUE_BASE_FIELD_TYPE_VALUES:
        return cast(CustomFieldValueBaseFieldType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELD_VALUE_BASE_FIELD_TYPE_VALUES!r}")
