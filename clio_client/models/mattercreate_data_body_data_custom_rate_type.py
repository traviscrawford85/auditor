from typing import Literal, cast

MattercreateDataBodyDataCustomRateType = Literal["ContingencyFee", "FlatRate", "HourlyRate"]

MATTERCREATE_DATA_BODY_DATA_CUSTOM_RATE_TYPE_VALUES: set[MattercreateDataBodyDataCustomRateType] = {
    "ContingencyFee",
    "FlatRate",
    "HourlyRate",
}


def check_mattercreate_data_body_data_custom_rate_type(value: str) -> MattercreateDataBodyDataCustomRateType:
    if value in MATTERCREATE_DATA_BODY_DATA_CUSTOM_RATE_TYPE_VALUES:
        return cast(MattercreateDataBodyDataCustomRateType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MATTERCREATE_DATA_BODY_DATA_CUSTOM_RATE_TYPE_VALUES!r}"
    )
