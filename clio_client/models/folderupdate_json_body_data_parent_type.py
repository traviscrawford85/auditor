from typing import Literal, cast

FolderupdateJsonBodyDataParentType = Literal["Contact", "Folder", "Matter"]

FOLDERUPDATE_JSON_BODY_DATA_PARENT_TYPE_VALUES: set[FolderupdateJsonBodyDataParentType] = {
    "Contact",
    "Folder",
    "Matter",
}


def check_folderupdate_json_body_data_parent_type(value: str) -> FolderupdateJsonBodyDataParentType:
    if value in FOLDERUPDATE_JSON_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(FolderupdateJsonBodyDataParentType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FOLDERUPDATE_JSON_BODY_DATA_PARENT_TYPE_VALUES!r}")
