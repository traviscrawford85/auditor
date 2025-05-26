from typing import Literal, cast

MatterupdateFilesBodyDataCustomRateType = Literal["ContingencyFee", "FlatRate", "HourlyRate"]

MATTERUPDATE_FILES_BODY_DATA_CUSTOM_RATE_TYPE_VALUES: set[MatterupdateFilesBodyDataCustomRateType] = {
    "ContingencyFee",
    "FlatRate",
    "HourlyRate",
}


def check_matterupdate_files_body_data_custom_rate_type(value: str) -> MatterupdateFilesBodyDataCustomRateType:
    if value in MATTERUPDATE_FILES_BODY_DATA_CUSTOM_RATE_TYPE_VALUES:
        return cast(MatterupdateFilesBodyDataCustomRateType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MATTERUPDATE_FILES_BODY_DATA_CUSTOM_RATE_TYPE_VALUES!r}"
    )
