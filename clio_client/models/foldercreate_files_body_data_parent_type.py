from typing import Literal, cast

FoldercreateFilesBodyDataParentType = Literal["Contact", "Folder", "Matter"]

FOLDERCREATE_FILES_BODY_DATA_PARENT_TYPE_VALUES: set[FoldercreateFilesBodyDataParentType] = {
    "Contact",
    "Folder",
    "Matter",
}


def check_foldercreate_files_body_data_parent_type(value: str) -> FoldercreateFilesBodyDataParentType:
    if value in FOLDERCREATE_FILES_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(FoldercreateFilesBodyDataParentType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FOLDERCREATE_FILES_BODY_DATA_PARENT_TYPE_VALUES!r}")
