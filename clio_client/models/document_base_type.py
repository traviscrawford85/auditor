from typing import Literal, cast

DocumentBaseType = Literal["Document"]

DOCUMENT_BASE_TYPE_VALUES: set[DocumentBaseType] = {
    "Document",
}


def check_document_base_type(value: str) -> DocumentBaseType:
    if value in DOCUMENT_BASE_TYPE_VALUES:
        return cast(DocumentBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOCUMENT_BASE_TYPE_VALUES!r}")
