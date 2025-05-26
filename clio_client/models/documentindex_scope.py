from typing import Literal, cast

DocumentindexScope = Literal["children", "descendants"]

DOCUMENTINDEX_SCOPE_VALUES: set[DocumentindexScope] = {
    "children",
    "descendants",
}


def check_documentindex_scope(value: str) -> DocumentindexScope:
    if value in DOCUMENTINDEX_SCOPE_VALUES:
        return cast(DocumentindexScope, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOCUMENTINDEX_SCOPE_VALUES!r}")
