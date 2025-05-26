from typing import Literal, cast

BillupdateDataBodyDataState = Literal["awaiting_approval", "awaiting_payment", "deleted", "draft", "paid", "void"]

BILLUPDATE_DATA_BODY_DATA_STATE_VALUES: set[BillupdateDataBodyDataState] = {
    "awaiting_approval",
    "awaiting_payment",
    "deleted",
    "draft",
    "paid",
    "void",
}


def check_billupdate_data_body_data_state(value: str) -> BillupdateDataBodyDataState:
    if value in BILLUPDATE_DATA_BODY_DATA_STATE_VALUES:
        return cast(BillupdateDataBodyDataState, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLUPDATE_DATA_BODY_DATA_STATE_VALUES!r}")
