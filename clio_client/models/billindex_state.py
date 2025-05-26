from typing import Literal, cast

BillindexState = Literal["awaiting_approval", "awaiting_payment", "deleted", "draft", "paid", "void"]

BILLINDEX_STATE_VALUES: set[BillindexState] = {
    "awaiting_approval",
    "awaiting_payment",
    "deleted",
    "draft",
    "paid",
    "void",
}


def check_billindex_state(value: str) -> BillindexState:
    if value in BILLINDEX_STATE_VALUES:
        return cast(BillindexState, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLINDEX_STATE_VALUES!r}")
