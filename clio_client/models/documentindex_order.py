from typing import Literal, cast

DocumentindexOrder = Literal[
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

DOCUMENTINDEX_ORDER_VALUES: set[DocumentindexOrder] = {
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


def check_documentindex_order(value: str) -> DocumentindexOrder:
    if value in DOCUMENTINDEX_ORDER_VALUES:
        return cast(DocumentindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOCUMENTINDEX_ORDER_VALUES!r}")
