from typing import Literal, cast

NoteBaseType = Literal["Contact", "Matter"]

NOTE_BASE_TYPE_VALUES: set[NoteBaseType] = {
    "Contact",
    "Matter",
}


def check_note_base_type(value: str) -> NoteBaseType:
    if value in NOTE_BASE_TYPE_VALUES:
        return cast(NoteBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTE_BASE_TYPE_VALUES!r}")
