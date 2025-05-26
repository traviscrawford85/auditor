from typing import Literal, cast

ActivityDescriptionupdateDataBodyDataRateType = Literal["Custom", "FlatRate", "User"]

ACTIVITY_DESCRIPTIONUPDATE_DATA_BODY_DATA_RATE_TYPE_VALUES: set[ActivityDescriptionupdateDataBodyDataRateType] = {
    "Custom",
    "FlatRate",
    "User",
}


def check_activity_descriptionupdate_data_body_data_rate_type(
    value: str,
) -> ActivityDescriptionupdateDataBodyDataRateType:
    if value in ACTIVITY_DESCRIPTIONUPDATE_DATA_BODY_DATA_RATE_TYPE_VALUES:
        return cast(ActivityDescriptionupdateDataBodyDataRateType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTIVITY_DESCRIPTIONUPDATE_DATA_BODY_DATA_RATE_TYPE_VALUES!r}"
    )
