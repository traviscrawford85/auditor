from typing import Literal, cast

ActivityupdateDataBodyDataType = Literal["ExpenseEntry", "HardCostEntry", "SoftCostEntry", "TimeEntry"]

ACTIVITYUPDATE_DATA_BODY_DATA_TYPE_VALUES: set[ActivityupdateDataBodyDataType] = {
    "ExpenseEntry",
    "HardCostEntry",
    "SoftCostEntry",
    "TimeEntry",
}


def check_activityupdate_data_body_data_type(value: str) -> ActivityupdateDataBodyDataType:
    if value in ACTIVITYUPDATE_DATA_BODY_DATA_TYPE_VALUES:
        return cast(ActivityupdateDataBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITYUPDATE_DATA_BODY_DATA_TYPE_VALUES!r}")
