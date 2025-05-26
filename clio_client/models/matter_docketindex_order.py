from typing import Literal, cast

MatterDocketindexOrder = Literal["date(asc)", "date(desc)", "id(asc)", "id(desc)"]

MATTER_DOCKETINDEX_ORDER_VALUES: set[MatterDocketindexOrder] = {
    "date(asc)",
    "date(desc)",
    "id(asc)",
    "id(desc)",
}


def check_matter_docketindex_order(value: str) -> MatterDocketindexOrder:
    if value in MATTER_DOCKETINDEX_ORDER_VALUES:
        return cast(MatterDocketindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATTER_DOCKETINDEX_ORDER_VALUES!r}")
