from typing import Literal, cast

DocumentupdateDataBodyDataParentType = Literal["Contact", "Document", "Folder", "Matter"]

DOCUMENTUPDATE_DATA_BODY_DATA_PARENT_TYPE_VALUES: set[DocumentupdateDataBodyDataParentType] = {
    "Contact",
    "Document",
    "Folder",
    "Matter",
}


def check_documentupdate_data_body_data_parent_type(value: str) -> DocumentupdateDataBodyDataParentType:
    if value in DOCUMENTUPDATE_DATA_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(DocumentupdateDataBodyDataParentType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOCUMENTUPDATE_DATA_BODY_DATA_PARENT_TYPE_VALUES!r}")
