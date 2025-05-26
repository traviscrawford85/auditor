from typing import Literal, cast

UtbmsSetindexOrder = Literal["id(asc)", "id(desc)", "name(asc)", "name(desc)"]

UTBMS_SETINDEX_ORDER_VALUES: set[UtbmsSetindexOrder] = {
    "id(asc)",
    "id(desc)",
    "name(asc)",
    "name(desc)",
}


def check_utbms_setindex_order(value: str) -> UtbmsSetindexOrder:
    if value in UTBMS_SETINDEX_ORDER_VALUES:
        return cast(UtbmsSetindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UTBMS_SETINDEX_ORDER_VALUES!r}")
