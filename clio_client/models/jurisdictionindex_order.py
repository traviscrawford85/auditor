from typing import Literal, cast

JurisdictionindexOrder = Literal["description(asc)", "description(desc)", "id(asc)", "id(desc)"]

JURISDICTIONINDEX_ORDER_VALUES: set[JurisdictionindexOrder] = {
    "description(asc)",
    "description(desc)",
    "id(asc)",
    "id(desc)",
}


def check_jurisdictionindex_order(value: str) -> JurisdictionindexOrder:
    if value in JURISDICTIONINDEX_ORDER_VALUES:
        return cast(JurisdictionindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {JURISDICTIONINDEX_ORDER_VALUES!r}")
