from typing import Literal, cast

MatterDocketindexStatus = Literal["completed", "failed,", "in_progress,", "not_started,"]

MATTER_DOCKETINDEX_STATUS_VALUES: set[MatterDocketindexStatus] = {
    "completed",
    "failed,",
    "in_progress,",
    "not_started,",
}


def check_matter_docketindex_status(value: str) -> MatterDocketindexStatus:
    if value in MATTER_DOCKETINDEX_STATUS_VALUES:
        return cast(MatterDocketindexStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATTER_DOCKETINDEX_STATUS_VALUES!r}")
