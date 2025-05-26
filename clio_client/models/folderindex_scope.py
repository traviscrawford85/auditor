from typing import Literal, cast

FolderindexScope = Literal["children", "descendants"]

FOLDERINDEX_SCOPE_VALUES: set[FolderindexScope] = {
    "children",
    "descendants",
}


def check_folderindex_scope(value: str) -> FolderindexScope:
    if value in FOLDERINDEX_SCOPE_VALUES:
        return cast(FolderindexScope, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FOLDERINDEX_SCOPE_VALUES!r}")
