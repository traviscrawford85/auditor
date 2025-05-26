from typing import Literal, cast

MatterindexPendingDate = Literal["<=DATE", "<DATE", "=DATE", ">=DATE", ">DATE"]

MATTERINDEX_PENDING_DATE_VALUES: set[MatterindexPendingDate] = {
    "<=DATE",
    "<DATE",
    "=DATE",
    ">=DATE",
    ">DATE",
}


def check_matterindex_pending_date(value: str) -> MatterindexPendingDate:
    if value in MATTERINDEX_PENDING_DATE_VALUES:
        return cast(MatterindexPendingDate, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATTERINDEX_PENDING_DATE_VALUES!r}")
