from typing import Literal, cast

MattercreateFilesBodyDataStatuteOfLimitationsStatus = Literal["complete", "in_progress", "in_review", "pending"]

MATTERCREATE_FILES_BODY_DATA_STATUTE_OF_LIMITATIONS_STATUS_VALUES: set[
    MattercreateFilesBodyDataStatuteOfLimitationsStatus
] = {
    "complete",
    "in_progress",
    "in_review",
    "pending",
}


def check_mattercreate_files_body_data_statute_of_limitations_status(
    value: str,
) -> MattercreateFilesBodyDataStatuteOfLimitationsStatus:
    if value in MATTERCREATE_FILES_BODY_DATA_STATUTE_OF_LIMITATIONS_STATUS_VALUES:
        return cast(MattercreateFilesBodyDataStatuteOfLimitationsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MATTERCREATE_FILES_BODY_DATA_STATUTE_OF_LIMITATIONS_STATUS_VALUES!r}"
    )
