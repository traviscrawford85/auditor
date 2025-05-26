from typing import Literal, cast

CommunicationindexOrder = Literal[
    "date(asc)",
    "date(desc)",
    "id(asc)",
    "id(desc)",
    "matter(asc)",
    "matter(desc)",
    "received_at(asc)",
    "received_at(desc)",
]

COMMUNICATIONINDEX_ORDER_VALUES: set[CommunicationindexOrder] = {
    "date(asc)",
    "date(desc)",
    "id(asc)",
    "id(desc)",
    "matter(asc)",
    "matter(desc)",
    "received_at(asc)",
    "received_at(desc)",
}


def check_communicationindex_order(value: str) -> CommunicationindexOrder:
    if value in COMMUNICATIONINDEX_ORDER_VALUES:
        return cast(CommunicationindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMMUNICATIONINDEX_ORDER_VALUES!r}")
