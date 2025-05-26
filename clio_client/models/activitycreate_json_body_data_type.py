from typing import Literal, cast

ActivitycreateJsonBodyDataType = Literal["ExpenseEntry", "HardCostEntry", "SoftCostEntry", "TimeEntry"]

ACTIVITYCREATE_JSON_BODY_DATA_TYPE_VALUES: set[ActivitycreateJsonBodyDataType] = {
    "ExpenseEntry",
    "HardCostEntry",
    "SoftCostEntry",
    "TimeEntry",
}


def check_activitycreate_json_body_data_type(value: str) -> ActivitycreateJsonBodyDataType:
    if value in ACTIVITYCREATE_JSON_BODY_DATA_TYPE_VALUES:
        return cast(ActivitycreateJsonBodyDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITYCREATE_JSON_BODY_DATA_TYPE_VALUES!r}")
