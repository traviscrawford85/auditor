from typing import Literal, cast

ActivityBaseType = Literal["ExpenseEntry", "HardCostEntry", "SoftCostEntry", "TimeEntry"]

ACTIVITY_BASE_TYPE_VALUES: set[ActivityBaseType] = {
    "ExpenseEntry",
    "HardCostEntry",
    "SoftCostEntry",
    "TimeEntry",
}


def check_activity_base_type(value: str) -> ActivityBaseType:
    if value in ACTIVITY_BASE_TYPE_VALUES:
        return cast(ActivityBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITY_BASE_TYPE_VALUES!r}")
