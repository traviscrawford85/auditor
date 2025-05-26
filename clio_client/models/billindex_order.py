from typing import Literal, cast

BillindexOrder = Literal[
    "balance(asc)",
    "balance(desc)",
    "client_name(asc)",
    "client_name(desc)",
    "due_at(asc)",
    "due_at(desc)",
    "id(asc)",
    "id(desc)",
    "issued_at(asc)",
    "issued_at(desc)",
    "last_sent_at(asc)",
    "last_sent_at(desc)",
    "matter_display_number(asc)",
    "matter_display_number(desc)",
    "number(asc)",
    "number(desc)",
    "paid_at(asc)",
    "paid_at(desc)",
]

BILLINDEX_ORDER_VALUES: set[BillindexOrder] = {
    "balance(asc)",
    "balance(desc)",
    "client_name(asc)",
    "client_name(desc)",
    "due_at(asc)",
    "due_at(desc)",
    "id(asc)",
    "id(desc)",
    "issued_at(asc)",
    "issued_at(desc)",
    "last_sent_at(asc)",
    "last_sent_at(desc)",
    "matter_display_number(asc)",
    "matter_display_number(desc)",
    "number(asc)",
    "number(desc)",
    "paid_at(asc)",
    "paid_at(desc)",
}


def check_billindex_order(value: str) -> BillindexOrder:
    if value in BILLINDEX_ORDER_VALUES:
        return cast(BillindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLINDEX_ORDER_VALUES!r}")
