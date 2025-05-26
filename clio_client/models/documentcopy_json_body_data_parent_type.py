from typing import Literal, cast

DocumentcopyJsonBodyDataParentType = Literal["Contact", "Document", "Folder", "Matter"]

DOCUMENTCOPY_JSON_BODY_DATA_PARENT_TYPE_VALUES: set[DocumentcopyJsonBodyDataParentType] = {
    "Contact",
    "Document",
    "Folder",
    "Matter",
}


def check_documentcopy_json_body_data_parent_type(value: str) -> DocumentcopyJsonBodyDataParentType:
    if value in DOCUMENTCOPY_JSON_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(DocumentcopyJsonBodyDataParentType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOCUMENTCOPY_JSON_BODY_DATA_PARENT_TYPE_VALUES!r}")
