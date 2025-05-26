from typing import Literal, cast

MattercreateDataBodyDataStatus = Literal["closed", "open", "pending"]

MATTERCREATE_DATA_BODY_DATA_STATUS_VALUES: set[MattercreateDataBodyDataStatus] = {
    "closed",
    "open",
    "pending",
}


def check_mattercreate_data_body_data_status(value: str) -> MattercreateDataBodyDataStatus:
    if value in MATTERCREATE_DATA_BODY_DATA_STATUS_VALUES:
        return cast(MattercreateDataBodyDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATTERCREATE_DATA_BODY_DATA_STATUS_VALUES!r}")
