from typing import Literal, cast

ClioPaymentsPaymentindexState = Literal[
    "authorized",
    "canceled",
    "completed",
    "completed_requiring_allocation",
    "failed",
    "pending",
    "requires_confirmation",
    "voided",
]

CLIO_PAYMENTS_PAYMENTINDEX_STATE_VALUES: set[ClioPaymentsPaymentindexState] = {
    "authorized",
    "canceled",
    "completed",
    "completed_requiring_allocation",
    "failed",
    "pending",
    "requires_confirmation",
    "voided",
}


def check_clio_payments_paymentindex_state(value: str) -> ClioPaymentsPaymentindexState:
    if value in CLIO_PAYMENTS_PAYMENTINDEX_STATE_VALUES:
        return cast(ClioPaymentsPaymentindexState, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CLIO_PAYMENTS_PAYMENTINDEX_STATE_VALUES!r}")
