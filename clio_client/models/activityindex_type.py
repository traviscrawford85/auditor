from typing import Literal, cast

ActivityindexType = Literal["ExpenseEntry", "HardCostEntry", "SoftCostEntry", "TimeEntry"]

ACTIVITYINDEX_TYPE_VALUES: set[ActivityindexType] = {
    "ExpenseEntry",
    "HardCostEntry",
    "SoftCostEntry",
    "TimeEntry",
}


def check_activityindex_type(value: str) -> ActivityindexType:
    if value in ACTIVITYINDEX_TYPE_VALUES:
        return cast(ActivityindexType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITYINDEX_TYPE_VALUES!r}")
