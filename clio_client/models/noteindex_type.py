from typing import Literal, cast

NoteindexType = Literal["Contact", "Matter"]

NOTEINDEX_TYPE_VALUES: set[NoteindexType] = {
    "Contact",
    "Matter",
}


def check_noteindex_type(value: str) -> NoteindexType:
    if value in NOTEINDEX_TYPE_VALUES:
        return cast(NoteindexType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTEINDEX_TYPE_VALUES!r}")
