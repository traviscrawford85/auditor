from typing import Literal, cast

ActivityDescriptionRateBaseType = Literal["Custom", "FlatRate", "User"]

ACTIVITY_DESCRIPTION_RATE_BASE_TYPE_VALUES: set[ActivityDescriptionRateBaseType] = {
    "Custom",
    "FlatRate",
    "User",
}


def check_activity_description_rate_base_type(value: str) -> ActivityDescriptionRateBaseType:
    if value in ACTIVITY_DESCRIPTION_RATE_BASE_TYPE_VALUES:
        return cast(ActivityDescriptionRateBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITY_DESCRIPTION_RATE_BASE_TYPE_VALUES!r}")
