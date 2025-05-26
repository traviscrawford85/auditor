from typing import Literal, cast

CustomFieldindexFieldType = Literal[
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

CUSTOM_FIELDINDEX_FIELD_TYPE_VALUES: set[CustomFieldindexFieldType] = {
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


def check_custom_fieldindex_field_type(value: str) -> CustomFieldindexFieldType:
    if value in CUSTOM_FIELDINDEX_FIELD_TYPE_VALUES:
        return cast(CustomFieldindexFieldType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELDINDEX_FIELD_TYPE_VALUES!r}")
