from typing import Literal, cast

LinkedFolderBaseType = Literal["Folder"]

LINKED_FOLDER_BASE_TYPE_VALUES: set[LinkedFolderBaseType] = {
    "Folder",
}


def check_linked_folder_base_type(value: str) -> LinkedFolderBaseType:
    if value in LINKED_FOLDER_BASE_TYPE_VALUES:
        return cast(LinkedFolderBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LINKED_FOLDER_BASE_TYPE_VALUES!r}")
