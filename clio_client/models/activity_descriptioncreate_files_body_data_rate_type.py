from typing import Literal, cast

ActivityDescriptioncreateFilesBodyDataRateType = Literal["Custom", "FlatRate", "User"]

ACTIVITY_DESCRIPTIONCREATE_FILES_BODY_DATA_RATE_TYPE_VALUES: set[ActivityDescriptioncreateFilesBodyDataRateType] = {
    "Custom",
    "FlatRate",
    "User",
}


def check_activity_descriptioncreate_files_body_data_rate_type(
    value: str,
) -> ActivityDescriptioncreateFilesBodyDataRateType:
    if value in ACTIVITY_DESCRIPTIONCREATE_FILES_BODY_DATA_RATE_TYPE_VALUES:
        return cast(ActivityDescriptioncreateFilesBodyDataRateType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ACTIVITY_DESCRIPTIONCREATE_FILES_BODY_DATA_RATE_TYPE_VALUES!r}"
    )
