from typing import Literal, cast

NoteindexOrder = Literal[
    "author(asc)",
    "author(desc)",
    "date(asc)",
    "date(desc)",
    "detail(asc)",
    "detail(desc)",
    "id(asc)",
    "id(desc)",
    "subject(asc)",
    "subject(desc)",
]

NOTEINDEX_ORDER_VALUES: set[NoteindexOrder] = {
    "author(asc)",
    "author(desc)",
    "date(asc)",
    "date(desc)",
    "detail(asc)",
    "detail(desc)",
    "id(asc)",
    "id(desc)",
    "subject(asc)",
    "subject(desc)",
}


def check_noteindex_order(value: str) -> NoteindexOrder:
    if value in NOTEINDEX_ORDER_VALUES:
        return cast(NoteindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTEINDEX_ORDER_VALUES!r}")
