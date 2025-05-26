from typing import Literal, cast

BillindexType = Literal["revenue", "trust"]

BILLINDEX_TYPE_VALUES: set[BillindexType] = {
    "revenue",
    "trust",
}


def check_billindex_type(value: str) -> BillindexType:
    if value in BILLINDEX_TYPE_VALUES:
        return cast(BillindexType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLINDEX_TYPE_VALUES!r}")
