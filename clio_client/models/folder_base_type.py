from typing import Literal, cast

FolderBaseType = Literal["Folder"]

FOLDER_BASE_TYPE_VALUES: set[FolderBaseType] = {
    "Folder",
}


def check_folder_base_type(value: str) -> FolderBaseType:
    if value in FOLDER_BASE_TYPE_VALUES:
        return cast(FolderBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FOLDER_BASE_TYPE_VALUES!r}")
