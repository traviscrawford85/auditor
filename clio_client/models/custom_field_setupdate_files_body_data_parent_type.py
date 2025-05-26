from typing import Literal, cast

CustomFieldSetupdateFilesBodyDataParentType = Literal["Contact", "Matter"]

CUSTOM_FIELD_SETUPDATE_FILES_BODY_DATA_PARENT_TYPE_VALUES: set[CustomFieldSetupdateFilesBodyDataParentType] = {
    "Contact",
    "Matter",
}


def check_custom_field_setupdate_files_body_data_parent_type(value: str) -> CustomFieldSetupdateFilesBodyDataParentType:
    if value in CUSTOM_FIELD_SETUPDATE_FILES_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(CustomFieldSetupdateFilesBodyDataParentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CUSTOM_FIELD_SETUPDATE_FILES_BODY_DATA_PARENT_TYPE_VALUES!r}"
    )
