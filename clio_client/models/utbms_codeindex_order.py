from typing import Literal, cast

UtbmsCodeindexOrder = Literal["id(asc)", "id(desc)", "name(asc)", "name(desc)", "set(asc)", "set(desc)"]

UTBMS_CODEINDEX_ORDER_VALUES: set[UtbmsCodeindexOrder] = {
    "id(asc)",
    "id(desc)",
    "name(asc)",
    "name(desc)",
    "set(asc)",
    "set(desc)",
}


def check_utbms_codeindex_order(value: str) -> UtbmsCodeindexOrder:
    if value in UTBMS_CODEINDEX_ORDER_VALUES:
        return cast(UtbmsCodeindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UTBMS_CODEINDEX_ORDER_VALUES!r}")
