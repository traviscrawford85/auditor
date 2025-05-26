from typing import Literal, cast

BillBaseState = Literal["awaiting_approval", "awaiting_payment", "deleted", "draft", "paid", "void"]

BILL_BASE_STATE_VALUES: set[BillBaseState] = {
    "awaiting_approval",
    "awaiting_payment",
    "deleted",
    "draft",
    "paid",
    "void",
}


def check_bill_base_state(value: str) -> BillBaseState:
    if value in BILL_BASE_STATE_VALUES:
        return cast(BillBaseState, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILL_BASE_STATE_VALUES!r}")
