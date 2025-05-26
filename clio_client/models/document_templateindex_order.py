from typing import Literal, cast

DocumentTemplateindexOrder = Literal[
    "category.name(asc)",
    "category.name(desc)",
    "filename(asc)",
    "filename(desc)",
    "id(asc)",
    "id(desc)",
    "last_modified(asc)",
    "last_modified(desc)",
    "last_modified_by.name(asc)",
    "last_modified_by.name(desc)",
]

DOCUMENT_TEMPLATEINDEX_ORDER_VALUES: set[DocumentTemplateindexOrder] = {
    "category.name(asc)",
    "category.name(desc)",
    "filename(asc)",
    "filename(desc)",
    "id(asc)",
    "id(desc)",
    "last_modified(asc)",
    "last_modified(desc)",
    "last_modified_by.name(asc)",
    "last_modified_by.name(desc)",
}


def check_document_templateindex_order(value: str) -> DocumentTemplateindexOrder:
    if value in DOCUMENT_TEMPLATEINDEX_ORDER_VALUES:
        return cast(DocumentTemplateindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOCUMENT_TEMPLATEINDEX_ORDER_VALUES!r}")
