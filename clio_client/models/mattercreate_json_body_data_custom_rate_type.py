from typing import Literal, cast

MattercreateJsonBodyDataCustomRateType = Literal["ContingencyFee", "FlatRate", "HourlyRate"]

MATTERCREATE_JSON_BODY_DATA_CUSTOM_RATE_TYPE_VALUES: set[MattercreateJsonBodyDataCustomRateType] = {
    "ContingencyFee",
    "FlatRate",
    "HourlyRate",
}


def check_mattercreate_json_body_data_custom_rate_type(value: str) -> MattercreateJsonBodyDataCustomRateType:
    if value in MATTERCREATE_JSON_BODY_DATA_CUSTOM_RATE_TYPE_VALUES:
        return cast(MattercreateJsonBodyDataCustomRateType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MATTERCREATE_JSON_BODY_DATA_CUSTOM_RATE_TYPE_VALUES!r}"
    )
