from typing import Literal, cast

BillupdateFilesBodyDataState = Literal["awaiting_approval", "awaiting_payment", "deleted", "draft", "paid", "void"]

BILLUPDATE_FILES_BODY_DATA_STATE_VALUES: set[BillupdateFilesBodyDataState] = {
    "awaiting_approval",
    "awaiting_payment",
    "deleted",
    "draft",
    "paid",
    "void",
}


def check_billupdate_files_body_data_state(value: str) -> BillupdateFilesBodyDataState:
    if value in BILLUPDATE_FILES_BODY_DATA_STATE_VALUES:
        return cast(BillupdateFilesBodyDataState, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLUPDATE_FILES_BODY_DATA_STATE_VALUES!r}")
