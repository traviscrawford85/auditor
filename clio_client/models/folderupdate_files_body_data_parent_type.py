from typing import Literal, cast

FolderupdateFilesBodyDataParentType = Literal["Contact", "Folder", "Matter"]

FOLDERUPDATE_FILES_BODY_DATA_PARENT_TYPE_VALUES: set[FolderupdateFilesBodyDataParentType] = {
    "Contact",
    "Folder",
    "Matter",
}


def check_folderupdate_files_body_data_parent_type(value: str) -> FolderupdateFilesBodyDataParentType:
    if value in FOLDERUPDATE_FILES_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(FolderupdateFilesBodyDataParentType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FOLDERUPDATE_FILES_BODY_DATA_PARENT_TYPE_VALUES!r}")
