from typing import Literal, cast

CustomFieldSetcreateFilesBodyDataParentType = Literal["Contact", "Matter"]

CUSTOM_FIELD_SETCREATE_FILES_BODY_DATA_PARENT_TYPE_VALUES: set[CustomFieldSetcreateFilesBodyDataParentType] = {
    "Contact",
    "Matter",
}


def check_custom_field_setcreate_files_body_data_parent_type(value: str) -> CustomFieldSetcreateFilesBodyDataParentType:
    if value in CUSTOM_FIELD_SETCREATE_FILES_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(CustomFieldSetcreateFilesBodyDataParentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELD_SETCREATE_FILES_BODY_DATA_PARENT_TYPE_VALUES!r}"
    )
