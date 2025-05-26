from typing import Literal, cast

TrustLineItemindexOrder = Literal["id(asc)", "id(desc)"]

TRUST_LINE_ITEMINDEX_ORDER_VALUES: set[TrustLineItemindexOrder] = {
    "id(asc)",
    "id(desc)",
}


def check_trust_line_itemindex_order(value: str) -> TrustLineItemindexOrder:
    if value in TRUST_LINE_ITEMINDEX_ORDER_VALUES:
        return cast(TrustLineItemindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRUST_LINE_ITEMINDEX_ORDER_VALUES!r}")
