from typing import Literal, cast

DocumentcopyFilesBodyDataParentType = Literal["Contact", "Document", "Folder", "Matter"]

DOCUMENTCOPY_FILES_BODY_DATA_PARENT_TYPE_VALUES: set[DocumentcopyFilesBodyDataParentType] = {
    "Contact",
    "Document",
    "Folder",
    "Matter",
}


def check_documentcopy_files_body_data_parent_type(value: str) -> DocumentcopyFilesBodyDataParentType:
    if value in DOCUMENTCOPY_FILES_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(DocumentcopyFilesBodyDataParentType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOCUMENTCOPY_FILES_BODY_DATA_PARENT_TYPE_VALUES!r}")
