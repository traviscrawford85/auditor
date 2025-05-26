from typing import Literal, cast

ContactindexOrder = Literal["id(asc)", "id(desc)", "name(asc)", "name(desc)", "shared_at(asc)", "shared_at(desc)"]

CONTACTINDEX_ORDER_VALUES: set[ContactindexOrder] = {
    "id(asc)",
    "id(desc)",
    "name(asc)",
    "name(desc)",
    "shared_at(asc)",
    "shared_at(desc)",
}


def check_contactindex_order(value: str) -> ContactindexOrder:
    if value in CONTACTINDEX_ORDER_VALUES:
        return cast(ContactindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACTINDEX_ORDER_VALUES!r}")
