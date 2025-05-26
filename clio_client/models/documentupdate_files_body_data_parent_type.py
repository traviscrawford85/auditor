from typing import Literal, cast

DocumentupdateFilesBodyDataParentType = Literal["Contact", "Document", "Folder", "Matter"]

DOCUMENTUPDATE_FILES_BODY_DATA_PARENT_TYPE_VALUES: set[DocumentupdateFilesBodyDataParentType] = {
    "Contact",
    "Document",
    "Folder",
    "Matter",
}


def check_documentupdate_files_body_data_parent_type(value: str) -> DocumentupdateFilesBodyDataParentType:
    if value in DOCUMENTUPDATE_FILES_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(DocumentupdateFilesBodyDataParentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DOCUMENTUPDATE_FILES_BODY_DATA_PARENT_TYPE_VALUES!r}"
    )
