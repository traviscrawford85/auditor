from typing import Literal, cast

MatterupdateJsonBodyDataStatuteOfLimitationsStatus = Literal["complete", "in_progress", "in_review", "pending"]

MATTERUPDATE_JSON_BODY_DATA_STATUTE_OF_LIMITATIONS_STATUS_VALUES: set[
    MatterupdateJsonBodyDataStatuteOfLimitationsStatus
] = {
    "complete",
    "in_progress",
    "in_review",
    "pending",
}


def check_matterupdate_json_body_data_statute_of_limitations_status(
    value: str,
) -> MatterupdateJsonBodyDataStatuteOfLimitationsStatus:
    if value in MATTERUPDATE_JSON_BODY_DATA_STATUTE_OF_LIMITATIONS_STATUS_VALUES:
        return cast(MatterupdateJsonBodyDataStatuteOfLimitationsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MATTERUPDATE_JSON_BODY_DATA_STATUTE_OF_LIMITATIONS_STATUS_VALUES!r}"
    )
