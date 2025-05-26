from typing import Literal, cast

ClioPaymentsPaymentBaseState = Literal[
    "authorized",
    "canceled",
    "completed",
    "completed_requiring_allocation",
    "failed",
    "pending",
    "requires_confirmation",
    "voided",
]

CLIO_PAYMENTS_PAYMENT_BASE_STATE_VALUES: set[ClioPaymentsPaymentBaseState] = {
    "authorized",
    "canceled",
    "completed",
    "completed_requiring_allocation",
    "failed",
    "pending",
    "requires_confirmation",
    "voided",
}


def check_clio_payments_payment_base_state(value: str) -> ClioPaymentsPaymentBaseState:
    if value in CLIO_PAYMENTS_PAYMENT_BASE_STATE_VALUES:
        return cast(ClioPaymentsPaymentBaseState, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CLIO_PAYMENTS_PAYMENT_BASE_STATE_VALUES!r}")
