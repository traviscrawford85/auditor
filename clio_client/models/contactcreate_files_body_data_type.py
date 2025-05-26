from typing import Literal, cast

ContactcreateFilesBodyDataType = Literal["Company", "Person"]

CONTACTCREATE_FILES_BODY_DATA_TYPE_VALUES: set[ContactcreateFilesBodyDataType] = {
    "Company",
    "Person",
}


def check_contactcreate_files_body_data_type(value: str) -> ContactcreateFilesBodyDataType:
    if value in CONTACTCREATE_FILES_BODY_DATA_TYPE_VALUES:
        return cast(ContactcreateFilesBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACTCREATE_FILES_BODY_DATA_TYPE_VALUES!r}")
