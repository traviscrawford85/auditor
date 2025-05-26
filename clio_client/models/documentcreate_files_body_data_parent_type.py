from typing import Literal, cast

DocumentcreateFilesBodyDataParentType = Literal["Contact", "Document", "Folder", "Matter"]

DOCUMENTCREATE_FILES_BODY_DATA_PARENT_TYPE_VALUES: set[DocumentcreateFilesBodyDataParentType] = {
    "Contact",
    "Document",
    "Folder",
    "Matter",
}


def check_documentcreate_files_body_data_parent_type(value: str) -> DocumentcreateFilesBodyDataParentType:
    if value in DOCUMENTCREATE_FILES_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(DocumentcreateFilesBodyDataParentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOCUMENTCREATE_FILES_BODY_DATA_PARENT_TYPE_VALUES!r}"
    )
