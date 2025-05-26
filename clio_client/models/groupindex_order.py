from typing import Literal, cast

GroupindexOrder = Literal["id(asc)", "id(desc)", "name(asc)", "name(desc)"]

GROUPINDEX_ORDER_VALUES: set[GroupindexOrder] = {
    "id(asc)",
    "id(desc)",
    "name(asc)",
    "name(desc)",
}


def check_groupindex_order(value: str) -> GroupindexOrder:
    if value in GROUPINDEX_ORDER_VALUES:
        return cast(GroupindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GROUPINDEX_ORDER_VALUES!r}")
