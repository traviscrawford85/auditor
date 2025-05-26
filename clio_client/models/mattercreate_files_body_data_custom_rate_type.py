from typing import Literal, cast

MattercreateFilesBodyDataCustomRateType = Literal["ContingencyFee", "FlatRate", "HourlyRate"]

MATTERCREATE_FILES_BODY_DATA_CUSTOM_RATE_TYPE_VALUES: set[MattercreateFilesBodyDataCustomRateType] = {
    "ContingencyFee",
    "FlatRate",
    "HourlyRate",
}


def check_mattercreate_files_body_data_custom_rate_type(value: str) -> MattercreateFilesBodyDataCustomRateType:
    if value in MATTERCREATE_FILES_BODY_DATA_CUSTOM_RATE_TYPE_VALUES:
        return cast(MattercreateFilesBodyDataCustomRateType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MATTERCREATE_FILES_BODY_DATA_CUSTOM_RATE_TYPE_VALUES!r}"
    )
