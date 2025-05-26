from typing import Literal, cast

BillindexStatus = Literal["all", "overdue"]

BILLINDEX_STATUS_VALUES: set[BillindexStatus] = {
    "all",
    "overdue",
}


def check_billindex_status(value: str) -> BillindexStatus:
    if value in BILLINDEX_STATUS_VALUES:
        return cast(BillindexStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLINDEX_STATUS_VALUES!r}")
