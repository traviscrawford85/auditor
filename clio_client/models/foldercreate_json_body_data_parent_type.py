from typing import Literal, cast

FoldercreateJsonBodyDataParentType = Literal["Contact", "Folder", "Matter"]

FOLDERCREATE_JSON_BODY_DATA_PARENT_TYPE_VALUES: set[FoldercreateJsonBodyDataParentType] = {
    "Contact",
    "Folder",
    "Matter",
}


def check_foldercreate_json_body_data_parent_type(value: str) -> FoldercreateJsonBodyDataParentType:
    if value in FOLDERCREATE_JSON_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(FoldercreateJsonBodyDataParentType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FOLDERCREATE_JSON_BODY_DATA_PARENT_TYPE_VALUES!r}")
