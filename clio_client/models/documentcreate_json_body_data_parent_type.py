from typing import Literal, cast

DocumentcreateJsonBodyDataParentType = Literal["Contact", "Document", "Folder", "Matter"]

DOCUMENTCREATE_JSON_BODY_DATA_PARENT_TYPE_VALUES: set[DocumentcreateJsonBodyDataParentType] = {
    "Contact",
    "Document",
    "Folder",
    "Matter",
}


def check_documentcreate_json_body_data_parent_type(value: str) -> DocumentcreateJsonBodyDataParentType:
    if value in DOCUMENTCREATE_JSON_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(DocumentcreateJsonBodyDataParentType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOCUMENTCREATE_JSON_BODY_DATA_PARENT_TYPE_VALUES!r}")
