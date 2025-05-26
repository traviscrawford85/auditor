from typing import Literal, cast

ActivitycreateDataBodyDataType = Literal["ExpenseEntry", "HardCostEntry", "SoftCostEntry", "TimeEntry"]

ACTIVITYCREATE_DATA_BODY_DATA_TYPE_VALUES: set[ActivitycreateDataBodyDataType] = {
    "ExpenseEntry",
    "HardCostEntry",
    "SoftCostEntry",
    "TimeEntry",
}


def check_activitycreate_data_body_data_type(value: str) -> ActivitycreateDataBodyDataType:
    if value in ACTIVITYCREATE_DATA_BODY_DATA_TYPE_VALUES:
        return cast(ActivitycreateDataBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITYCREATE_DATA_BODY_DATA_TYPE_VALUES!r}")
