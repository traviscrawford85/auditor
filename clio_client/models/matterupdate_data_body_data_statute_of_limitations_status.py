from typing import Literal, cast

MatterupdateDataBodyDataStatuteOfLimitationsStatus = Literal["complete", "in_progress", "in_review", "pending"]

MATTERUPDATE_DATA_BODY_DATA_STATUTE_OF_LIMITATIONS_STATUS_VALUES: set[
    MatterupdateDataBodyDataStatuteOfLimitationsStatus
] = {
    "complete",
    "in_progress",
    "in_review",
    "pending",
}


def check_matterupdate_data_body_data_statute_of_limitations_status(
    value: str,
) -> MatterupdateDataBodyDataStatuteOfLimitationsStatus:
    if value in MATTERUPDATE_DATA_BODY_DATA_STATUTE_OF_LIMITATIONS_STATUS_VALUES:
        return cast(MatterupdateDataBodyDataStatuteOfLimitationsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MATTERUPDATE_DATA_BODY_DATA_STATUTE_OF_LIMITATIONS_STATUS_VALUES!r}"
    )
