from typing import Literal, cast

ActivityindexStatus = Literal["billable", "billed", "draft", "non_billable", "unbilled", "written_off"]

ACTIVITYINDEX_STATUS_VALUES: set[ActivityindexStatus] = {
    "billable",
    "billed",
    "draft",
    "non_billable",
    "unbilled",
    "written_off",
}


def check_activityindex_status(value: str) -> ActivityindexStatus:
    if value in ACTIVITYINDEX_STATUS_VALUES:
        return cast(ActivityindexStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITYINDEX_STATUS_VALUES!r}")
