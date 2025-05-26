from typing import Literal, cast

ItemBaseType = Literal["Document", "Folder"]

ITEM_BASE_TYPE_VALUES: set[ItemBaseType] = {
    "Document",
    "Folder",
}


def check_item_base_type(value: str) -> ItemBaseType:
    if value in ITEM_BASE_TYPE_VALUES:
        return cast(ItemBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ITEM_BASE_TYPE_VALUES!r}")
