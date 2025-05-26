from typing import Literal, cast

FolderlistScope = Literal["children", "descendants"]

FOLDERLIST_SCOPE_VALUES: set[FolderlistScope] = {
    "children",
    "descendants",
}


def check_folderlist_scope(value: str) -> FolderlistScope:
    if value in FOLDERLIST_SCOPE_VALUES:
        return cast(FolderlistScope, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FOLDERLIST_SCOPE_VALUES!r}")
