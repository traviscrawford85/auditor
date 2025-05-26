from typing import Literal, cast

MatterupdateJsonBodyDataStatus = Literal["closed", "open", "pending"]

MATTERUPDATE_JSON_BODY_DATA_STATUS_VALUES: set[MatterupdateJsonBodyDataStatus] = {
    "closed",
    "open",
    "pending",
}


def check_matterupdate_json_body_data_status(value: str) -> MatterupdateJsonBodyDataStatus:
    if value in MATTERUPDATE_JSON_BODY_DATA_STATUS_VALUES:
        return cast(MatterupdateJsonBodyDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATTERUPDATE_JSON_BODY_DATA_STATUS_VALUES!r}")
