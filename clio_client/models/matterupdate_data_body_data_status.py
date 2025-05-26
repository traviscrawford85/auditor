from typing import Literal, cast

MatterupdateDataBodyDataStatus = Literal["closed", "open", "pending"]

MATTERUPDATE_DATA_BODY_DATA_STATUS_VALUES: set[MatterupdateDataBodyDataStatus] = {
    "closed",
    "open",
    "pending",
}


def check_matterupdate_data_body_data_status(value: str) -> MatterupdateDataBodyDataStatus:
    if value in MATTERUPDATE_DATA_BODY_DATA_STATUS_VALUES:
        return cast(MatterupdateDataBodyDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATTERUPDATE_DATA_BODY_DATA_STATUS_VALUES!r}")
