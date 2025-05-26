from typing import Literal, cast

DocumentcreateDataBodyDataParentType = Literal["Contact", "Document", "Folder", "Matter"]

DOCUMENTCREATE_DATA_BODY_DATA_PARENT_TYPE_VALUES: set[DocumentcreateDataBodyDataParentType] = {
    "Contact",
    "Document",
    "Folder",
    "Matter",
}


def check_documentcreate_data_body_data_parent_type(value: str) -> DocumentcreateDataBodyDataParentType:
    if value in DOCUMENTCREATE_DATA_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(DocumentcreateDataBodyDataParentType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOCUMENTCREATE_DATA_BODY_DATA_PARENT_TYPE_VALUES!r}")
