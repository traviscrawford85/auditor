from typing import Literal, cast

CustomFieldcreateJsonBodyDataFieldType = Literal[
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

CUSTOM_FIELDCREATE_JSON_BODY_DATA_FIELD_TYPE_VALUES: set[CustomFieldcreateJsonBodyDataFieldType] = {
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


def check_custom_fieldcreate_json_body_data_field_type(value: str) -> CustomFieldcreateJsonBodyDataFieldType:
    if value in CUSTOM_FIELDCREATE_JSON_BODY_DATA_FIELD_TYPE_VALUES:
        return cast(CustomFieldcreateJsonBodyDataFieldType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELDCREATE_JSON_BODY_DATA_FIELD_TYPE_VALUES!r}"
    )
