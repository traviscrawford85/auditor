from typing import Literal, cast

ActivityDescriptioncreateDataBodyDataRateType = Literal["Custom", "FlatRate", "User"]

ACTIVITY_DESCRIPTIONCREATE_DATA_BODY_DATA_RATE_TYPE_VALUES: set[ActivityDescriptioncreateDataBodyDataRateType] = {
    "Custom",
    "FlatRate",
    "User",
}


def check_activity_descriptioncreate_data_body_data_rate_type(
    value: str,
) -> ActivityDescriptioncreateDataBodyDataRateType:
    if value in ACTIVITY_DESCRIPTIONCREATE_DATA_BODY_DATA_RATE_TYPE_VALUES:
        return cast(ActivityDescriptioncreateDataBodyDataRateType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTIVITY_DESCRIPTIONCREATE_DATA_BODY_DATA_RATE_TYPE_VALUES!r}"
    )
