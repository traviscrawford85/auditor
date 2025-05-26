from typing import Literal, cast

CustomFieldcreateDataBodyDataFieldType = Literal[
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

CUSTOM_FIELDCREATE_DATA_BODY_DATA_FIELD_TYPE_VALUES: set[CustomFieldcreateDataBodyDataFieldType] = {
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


def check_custom_fieldcreate_data_body_data_field_type(value: str) -> CustomFieldcreateDataBodyDataFieldType:
    if value in CUSTOM_FIELDCREATE_DATA_BODY_DATA_FIELD_TYPE_VALUES:
        return cast(CustomFieldcreateDataBodyDataFieldType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELDCREATE_DATA_BODY_DATA_FIELD_TYPE_VALUES!r}"
    )
