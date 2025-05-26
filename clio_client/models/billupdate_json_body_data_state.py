from typing import Literal, cast

BillupdateJsonBodyDataState = Literal["awaiting_approval", "awaiting_payment", "deleted", "draft", "paid", "void"]

BILLUPDATE_JSON_BODY_DATA_STATE_VALUES: set[BillupdateJsonBodyDataState] = {
    "awaiting_approval",
    "awaiting_payment",
    "deleted",
    "draft",
    "paid",
    "void",
}


def check_billupdate_json_body_data_state(value: str) -> BillupdateJsonBodyDataState:
    if value in BILLUPDATE_JSON_BODY_DATA_STATE_VALUES:
        return cast(BillupdateJsonBodyDataState, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLUPDATE_JSON_BODY_DATA_STATE_VALUES!r}")
