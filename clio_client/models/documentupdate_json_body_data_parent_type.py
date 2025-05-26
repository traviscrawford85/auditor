from typing import Literal, cast

DocumentupdateJsonBodyDataParentType = Literal["Contact", "Document", "Folder", "Matter"]

DOCUMENTUPDATE_JSON_BODY_DATA_PARENT_TYPE_VALUES: set[DocumentupdateJsonBodyDataParentType] = {
    "Contact",
    "Document",
    "Folder",
    "Matter",
}


def check_documentupdate_json_body_data_parent_type(value: str) -> DocumentupdateJsonBodyDataParentType:
    if value in DOCUMENTUPDATE_JSON_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(DocumentupdateJsonBodyDataParentType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOCUMENTUPDATE_JSON_BODY_DATA_PARENT_TYPE_VALUES!r}")
