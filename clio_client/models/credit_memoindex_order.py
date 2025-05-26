from typing import Literal, cast

CreditMemoindexOrder = Literal["date(asc)", "date(desc)", "id(asc)", "id(desc)"]

CREDIT_MEMOINDEX_ORDER_VALUES: set[CreditMemoindexOrder] = {
    "date(asc)",
    "date(desc)",
    "id(asc)",
    "id(desc)",
}


def check_credit_memoindex_order(value: str) -> CreditMemoindexOrder:
    if value in CREDIT_MEMOINDEX_ORDER_VALUES:
        return cast(CreditMemoindexOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREDIT_MEMOINDEX_ORDER_VALUES!r}")
