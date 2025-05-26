from typing import Literal, cast

AllocationindexOrder = Literal["date(asc)", "date(desc)", "id(asc)", "id(desc)"]

ALLOCATIONINDEX_ORDER_VALUES: set[AllocationindexOrder] = {
    "date(asc)",
    "date(desc)",
    "id(asc)",
    "id(desc)",
}


def check_allocationindex_order(value: str) -> AllocationindexOrder:
    if value in ALLOCATIONINDEX_ORDER_VALUES:
        return cast(AllocationindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALLOCATIONINDEX_ORDER_VALUES!r}")
