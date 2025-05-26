from typing import Literal, cast

MatterDocketindexMatterStatus = Literal["closed", "open", "pending"]

MATTER_DOCKETINDEX_MATTER_STATUS_VALUES: set[MatterDocketindexMatterStatus] = {
    "closed",
    "open",
    "pending",
}


def check_matter_docketindex_matter_status(value: str) -> MatterDocketindexMatterStatus:
    if value in MATTER_DOCKETINDEX_MATTER_STATUS_VALUES:
        return cast(MatterDocketindexMatterStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATTER_DOCKETINDEX_MATTER_STATUS_VALUES!r}")
