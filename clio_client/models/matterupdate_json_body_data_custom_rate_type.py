from typing import Literal, cast

MatterupdateJsonBodyDataCustomRateType = Literal["ContingencyFee", "FlatRate", "HourlyRate"]

MATTERUPDATE_JSON_BODY_DATA_CUSTOM_RATE_TYPE_VALUES: set[MatterupdateJsonBodyDataCustomRateType] = {
    "ContingencyFee",
    "FlatRate",
    "HourlyRate",
}


def check_matterupdate_json_body_data_custom_rate_type(value: str) -> MatterupdateJsonBodyDataCustomRateType:
    if value in MATTERUPDATE_JSON_BODY_DATA_CUSTOM_RATE_TYPE_VALUES:
        return cast(MatterupdateJsonBodyDataCustomRateType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MATTERUPDATE_JSON_BODY_DATA_CUSTOM_RATE_TYPE_VALUES!r}"
    )
