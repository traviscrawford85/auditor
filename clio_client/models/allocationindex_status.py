from typing import Literal, cast

AllocationindexStatus = Literal["invalid", "valid"]

ALLOCATIONINDEX_STATUS_VALUES: set[AllocationindexStatus] = {
    "invalid",
    "valid",
}


def check_allocationindex_status(value: str) -> AllocationindexStatus:
    if value in ALLOCATIONINDEX_STATUS_VALUES:
        return cast(AllocationindexStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ALLOCATIONINDEX_STATUS_VALUES!r}")
