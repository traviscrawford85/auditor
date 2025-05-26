from typing import Literal, cast

NotecreateFilesBodyDataType = Literal["Contact", "Matter"]

NOTECREATE_FILES_BODY_DATA_TYPE_VALUES: set[NotecreateFilesBodyDataType] = {
    "Contact",
    "Matter",
}


def check_notecreate_files_body_data_type(value: str) -> NotecreateFilesBodyDataType:
    if value in NOTECREATE_FILES_BODY_DATA_TYPE_VALUES:
        return cast(NotecreateFilesBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTECREATE_FILES_BODY_DATA_TYPE_VALUES!r}")
