from typing import Literal, cast

ActivityupdateJsonBodyDataType = Literal["ExpenseEntry", "HardCostEntry", "SoftCostEntry", "TimeEntry"]

ACTIVITYUPDATE_JSON_BODY_DATA_TYPE_VALUES: set[ActivityupdateJsonBodyDataType] = {
    "ExpenseEntry",
    "HardCostEntry",
    "SoftCostEntry",
    "TimeEntry",
}


def check_activityupdate_json_body_data_type(value: str) -> ActivityupdateJsonBodyDataType:
    if value in ACTIVITYUPDATE_JSON_BODY_DATA_TYPE_VALUES:
        return cast(ActivityupdateJsonBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITYUPDATE_JSON_BODY_DATA_TYPE_VALUES!r}")
