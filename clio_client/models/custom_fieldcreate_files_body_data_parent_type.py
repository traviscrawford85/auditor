from typing import Literal, cast

CustomFieldcreateFilesBodyDataParentType = Literal["Contact", "Matter"]

CUSTOM_FIELDCREATE_FILES_BODY_DATA_PARENT_TYPE_VALUES: set[CustomFieldcreateFilesBodyDataParentType] = {
    "Contact",
    "Matter",
}


def check_custom_fieldcreate_files_body_data_parent_type(value: str) -> CustomFieldcreateFilesBodyDataParentType:
    if value in CUSTOM_FIELDCREATE_FILES_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(CustomFieldcreateFilesBodyDataParentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELDCREATE_FILES_BODY_DATA_PARENT_TYPE_VALUES!r}"
    )
