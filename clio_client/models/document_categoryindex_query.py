from typing import Literal, cast

DocumentCategoryindexQuery = Literal["name"]

DOCUMENT_CATEGORYINDEX_QUERY_VALUES: set[DocumentCategoryindexQuery] = {
    "name",
}


def check_document_categoryindex_query(value: str) -> DocumentCategoryindexQuery:
    if value in DOCUMENT_CATEGORYINDEX_QUERY_VALUES:
        return cast(DocumentCategoryindexQuery, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOCUMENT_CATEGORYINDEX_QUERY_VALUES!r}")
