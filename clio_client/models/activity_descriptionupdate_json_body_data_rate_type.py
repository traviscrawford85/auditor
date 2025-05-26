from typing import Literal, cast

ActivityDescriptionupdateJsonBodyDataRateType = Literal["Custom", "FlatRate", "User"]

ACTIVITY_DESCRIPTIONUPDATE_JSON_BODY_DATA_RATE_TYPE_VALUES: set[ActivityDescriptionupdateJsonBodyDataRateType] = {
    "Custom",
    "FlatRate",
    "User",
}


def check_activity_descriptionupdate_json_body_data_rate_type(
    value: str,
) -> ActivityDescriptionupdateJsonBodyDataRateType:
    if value in ACTIVITY_DESCRIPTIONUPDATE_JSON_BODY_DATA_RATE_TYPE_VALUES:
        return cast(ActivityDescriptionupdateJsonBodyDataRateType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTIVITY_DESCRIPTIONUPDATE_JSON_BODY_DATA_RATE_TYPE_VALUES!r}"
    )
