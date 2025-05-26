from typing import Literal, cast

ContactupdateFilesBodyDataType = Literal["Company", "Person"]

CONTACTUPDATE_FILES_BODY_DATA_TYPE_VALUES: set[ContactupdateFilesBodyDataType] = {
    "Company",
    "Person",
}


def check_contactupdate_files_body_data_type(value: str) -> ContactupdateFilesBodyDataType:
    if value in CONTACTUPDATE_FILES_BODY_DATA_TYPE_VALUES:
        return cast(ContactupdateFilesBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACTUPDATE_FILES_BODY_DATA_TYPE_VALUES!r}")
