from typing import Literal, cast

DocumentcopyDataBodyDataParentType = Literal["Contact", "Document", "Folder", "Matter"]

DOCUMENTCOPY_DATA_BODY_DATA_PARENT_TYPE_VALUES: set[DocumentcopyDataBodyDataParentType] = {
    "Contact",
    "Document",
    "Folder",
    "Matter",
}


def check_documentcopy_data_body_data_parent_type(value: str) -> DocumentcopyDataBodyDataParentType:
    if value in DOCUMENTCOPY_DATA_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(DocumentcopyDataBodyDataParentType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOCUMENTCOPY_DATA_BODY_DATA_PARENT_TYPE_VALUES!r}")
