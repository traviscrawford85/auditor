from typing import Literal, cast

MatterindexStatus = Literal["closed", "open", "pending"]

MATTERINDEX_STATUS_VALUES: set[MatterindexStatus] = {
    "closed",
    "open",
    "pending",
}


def check_matterindex_status(value: str) -> MatterindexStatus:
    if value in MATTERINDEX_STATUS_VALUES:
        return cast(MatterindexStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATTERINDEX_STATUS_VALUES!r}")
