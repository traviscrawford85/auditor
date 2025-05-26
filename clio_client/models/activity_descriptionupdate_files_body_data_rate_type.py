from typing import Literal, cast

ActivityDescriptionupdateFilesBodyDataRateType = Literal["Custom", "FlatRate", "User"]

ACTIVITY_DESCRIPTIONUPDATE_FILES_BODY_DATA_RATE_TYPE_VALUES: set[ActivityDescriptionupdateFilesBodyDataRateType] = {
    "Custom",
    "FlatRate",
    "User",
}


def check_activity_descriptionupdate_files_body_data_rate_type(
    value: str,
) -> ActivityDescriptionupdateFilesBodyDataRateType:
    if value in ACTIVITY_DESCRIPTIONUPDATE_FILES_BODY_DATA_RATE_TYPE_VALUES:
        return cast(ActivityDescriptionupdateFilesBodyDataRateType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTIVITY_DESCRIPTIONUPDATE_FILES_BODY_DATA_RATE_TYPE_VALUES!r}"
    )
