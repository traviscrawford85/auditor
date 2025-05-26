from typing import Literal, cast

ActivityDescriptioncreateJsonBodyDataRateType = Literal["Custom", "FlatRate", "User"]

ACTIVITY_DESCRIPTIONCREATE_JSON_BODY_DATA_RATE_TYPE_VALUES: set[ActivityDescriptioncreateJsonBodyDataRateType] = {
    "Custom",
    "FlatRate",
    "User",
}


def check_activity_descriptioncreate_json_body_data_rate_type(
    value: str,
) -> ActivityDescriptioncreateJsonBodyDataRateType:
    if value in ACTIVITY_DESCRIPTIONCREATE_JSON_BODY_DATA_RATE_TYPE_VALUES:
        return cast(ActivityDescriptioncreateJsonBodyDataRateType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTIVITY_DESCRIPTIONCREATE_JSON_BODY_DATA_RATE_TYPE_VALUES!r}"
    )
