from typing import Literal, cast

MattercreateDataBodyDataStatuteOfLimitationsStatus = Literal["complete", "in_progress", "in_review", "pending"]

MATTERCREATE_DATA_BODY_DATA_STATUTE_OF_LIMITATIONS_STATUS_VALUES: set[
    MattercreateDataBodyDataStatuteOfLimitationsStatus
] = {
    "complete",
    "in_progress",
    "in_review",
    "pending",
}


def check_mattercreate_data_body_data_statute_of_limitations_status(
    value: str,
) -> MattercreateDataBodyDataStatuteOfLimitationsStatus:
    if value in MATTERCREATE_DATA_BODY_DATA_STATUTE_OF_LIMITATIONS_STATUS_VALUES:
        return cast(MattercreateDataBodyDataStatuteOfLimitationsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MATTERCREATE_DATA_BODY_DATA_STATUTE_OF_LIMITATIONS_STATUS_VALUES!r}"
    )
