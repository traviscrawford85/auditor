from typing import Literal, cast

DocumentCategoryindexOrder = Literal["id(asc)", "id(desc)", "name(asc)", "name(desc)"]

DOCUMENT_CATEGORYINDEX_ORDER_VALUES: set[DocumentCategoryindexOrder] = {
    "id(asc)",
    "id(desc)",
    "name(asc)",
    "name(desc)",
}


def check_document_categoryindex_order(value: str) -> DocumentCategoryindexOrder:
    if value in DOCUMENT_CATEGORYINDEX_ORDER_VALUES:
        return cast(DocumentCategoryindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOCUMENT_CATEGORYINDEX_ORDER_VALUES!r}")
