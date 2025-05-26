from typing import Literal, cast

FolderindexOrder = Literal["id(asc)", "id(desc)", "name(asc)", "name(desc)"]

FOLDERINDEX_ORDER_VALUES: set[FolderindexOrder] = {
    "id(asc)",
    "id(desc)",
    "name(asc)",
    "name(desc)",
}


def check_folderindex_order(value: str) -> FolderindexOrder:
    if value in FOLDERINDEX_ORDER_VALUES:
        return cast(FolderindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FOLDERINDEX_ORDER_VALUES!r}")
