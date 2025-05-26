from typing import Literal, cast

BillBaseAvailableStateTransitions = Literal["awaiting_approval", "awaiting_payment", "deleted", "paid", "void"]

BILL_BASE_AVAILABLE_STATE_TRANSITIONS_VALUES: set[BillBaseAvailableStateTransitions] = {
    "awaiting_approval",
    "awaiting_payment",
    "deleted",
    "paid",
    "void",
}


def check_bill_base_available_state_transitions(value: str) -> BillBaseAvailableStateTransitions:
    if value in BILL_BASE_AVAILABLE_STATE_TRANSITIONS_VALUES:
        return cast(BillBaseAvailableStateTransitions, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILL_BASE_AVAILABLE_STATE_TRANSITIONS_VALUES!r}")
