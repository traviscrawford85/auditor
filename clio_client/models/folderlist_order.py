from typing import Literal, cast

FolderlistOrder = Literal[
    "created_at(asc)",
    "created_at(desc)",
    "document_number(asc)",
    "document_number(desc)",
    "id(asc)",
    "id(desc)",
    "name(asc)",
    "name(desc)",
    "received_at(asc)",
    "received_at(desc)",
    "updated_at(asc)",
    "updated_at(desc)",
]

FOLDERLIST_ORDER_VALUES: set[FolderlistOrder] = {
    "created_at(asc)",
    "created_at(desc)",
    "document_number(asc)",
    "document_number(desc)",
    "id(asc)",
    "id(desc)",
    "name(asc)",
    "name(desc)",
    "received_at(asc)",
    "received_at(desc)",
    "updated_at(asc)",
    "updated_at(desc)",
}


def check_folderlist_order(value: str) -> FolderlistOrder:
    if value in FOLDERLIST_ORDER_VALUES:
        return cast(FolderlistOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FOLDERLIST_ORDER_VALUES!r}")
