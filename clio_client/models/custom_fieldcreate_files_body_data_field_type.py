from typing import Literal, cast

CustomFieldcreateFilesBodyDataFieldType = Literal[
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

CUSTOM_FIELDCREATE_FILES_BODY_DATA_FIELD_TYPE_VALUES: set[CustomFieldcreateFilesBodyDataFieldType] = {
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


def check_custom_fieldcreate_files_body_data_field_type(value: str) -> CustomFieldcreateFilesBodyDataFieldType:
    if value in CUSTOM_FIELDCREATE_FILES_BODY_DATA_FIELD_TYPE_VALUES:
        return cast(CustomFieldcreateFilesBodyDataFieldType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELDCREATE_FILES_BODY_DATA_FIELD_TYPE_VALUES!r}"
    )
