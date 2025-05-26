from typing import Literal, cast

MattercreateJsonBodyDataStatus = Literal["closed", "open", "pending"]

MATTERCREATE_JSON_BODY_DATA_STATUS_VALUES: set[MattercreateJsonBodyDataStatus] = {
    "closed",
    "open",
    "pending",
}


def check_mattercreate_json_body_data_status(value: str) -> MattercreateJsonBodyDataStatus:
    if value in MATTERCREATE_JSON_BODY_DATA_STATUS_VALUES:
        return cast(MattercreateJsonBodyDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATTERCREATE_JSON_BODY_DATA_STATUS_VALUES!r}")
