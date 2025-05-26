from typing import Literal, cast

DocumentAutomationindexOrder = Literal["id(asc)", "id(desc)"]

DOCUMENT_AUTOMATIONINDEX_ORDER_VALUES: set[DocumentAutomationindexOrder] = {
    "id(asc)",
    "id(desc)",
}


def check_document_automationindex_order(value: str) -> DocumentAutomationindexOrder:
    if value in DOCUMENT_AUTOMATIONINDEX_ORDER_VALUES:
        return cast(DocumentAutomationindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DOCUMENT_AUTOMATIONINDEX_ORDER_VALUES!r}")
