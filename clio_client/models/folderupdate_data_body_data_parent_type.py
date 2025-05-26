from typing import Literal, cast

FolderupdateDataBodyDataParentType = Literal["Contact", "Folder", "Matter"]

FOLDERUPDATE_DATA_BODY_DATA_PARENT_TYPE_VALUES: set[FolderupdateDataBodyDataParentType] = {
    "Contact",
    "Folder",
    "Matter",
}


def check_folderupdate_data_body_data_parent_type(value: str) -> FolderupdateDataBodyDataParentType:
    if value in FOLDERUPDATE_DATA_BODY_DATA_PARENT_TYPE_VALUES:
        return cast(FolderupdateDataBodyDataParentType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FOLDERUPDATE_DATA_BODY_DATA_PARENT_TYPE_VALUES!r}")
