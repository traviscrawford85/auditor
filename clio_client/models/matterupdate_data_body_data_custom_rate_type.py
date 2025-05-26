from typing import Literal, cast

MatterupdateDataBodyDataCustomRateType = Literal["ContingencyFee", "FlatRate", "HourlyRate"]

MATTERUPDATE_DATA_BODY_DATA_CUSTOM_RATE_TYPE_VALUES: set[MatterupdateDataBodyDataCustomRateType] = {
    "ContingencyFee",
    "FlatRate",
    "HourlyRate",
}


def check_matterupdate_data_body_data_custom_rate_type(value: str) -> MatterupdateDataBodyDataCustomRateType:
    if value in MATTERUPDATE_DATA_BODY_DATA_CUSTOM_RATE_TYPE_VALUES:
        return cast(MatterupdateDataBodyDataCustomRateType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MATTERUPDATE_DATA_BODY_DATA_CUSTOM_RATE_TYPE_VALUES!r}"
    )
