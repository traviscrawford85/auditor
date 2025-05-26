from typing import Literal, cast

FoldercreateDataBodyDataParentType = Literal["Contact", "Folder", "Matter"]

FOLDERCREATE_DATA_BODY_DATA_PARENT_TYPE_VALUES: set[FoldercreateDataBodyDataParentType] = {
    "Contact",
    "Folder",
    "Matter",
}


def check_foldercreate_data_body_data_parent_type(value: str) -> FoldercreateDataBodyDataParentType:
    if value in FOLDERCREATE_DATA_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(FoldercreateDataBodyDataParentType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FOLDERCREATE_DATA_BODY_DATA_PARENT_TYPE_VALUES!r}")
