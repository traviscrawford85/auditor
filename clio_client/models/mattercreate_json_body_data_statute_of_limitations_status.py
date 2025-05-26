from typing import Literal, cast

MattercreateJsonBodyDataStatuteOfLimitationsStatus = Literal["complete", "in_progress", "in_review", "pending"]

MATTERCREATE_JSON_BODY_DATA_STATUTE_OF_LIMITATIONS_STATUS_VALUES: set[
    MattercreateJsonBodyDataStatuteOfLimitationsStatus
] = {
    "complete",
    "in_progress",
    "in_review",
    "pending",
}


def check_mattercreate_json_body_data_statute_of_limitations_status(
    value: str,
) -> MattercreateJsonBodyDataStatuteOfLimitationsStatus:
    if value in MATTERCREATE_JSON_BODY_DATA_STATUTE_OF_LIMITATIONS_STATUS_VALUES:
        return cast(MattercreateJsonBodyDataStatuteOfLimitationsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MATTERCREATE_JSON_BODY_DATA_STATUTE_OF_LIMITATIONS_STATUS_VALUES!r}"
    )
