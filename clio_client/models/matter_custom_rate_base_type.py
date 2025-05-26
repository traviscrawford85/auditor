from typing import Literal, cast

MatterCustomRateBaseType = Literal["ContingencyFee", "FlatRate", "HourlyRate"]

MATTER_CUSTOM_RATE_BASE_TYPE_VALUES: set[MatterCustomRateBaseType] = {
    "ContingencyFee",
    "FlatRate",
    "HourlyRate",
}


def check_matter_custom_rate_base_type(value: str) -> MatterCustomRateBaseType:
    if value in MATTER_CUSTOM_RATE_BASE_TYPE_VALUES:
        return cast(MatterCustomRateBaseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATTER_CUSTOM_RATE_BASE_TYPE_VALUES!r}")
