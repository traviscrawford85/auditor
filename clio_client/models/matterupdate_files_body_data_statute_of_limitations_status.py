from typing import Literal, cast

MatterupdateFilesBodyDataStatuteOfLimitationsStatus = Literal["complete", "in_progress", "in_review", "pending"]

MATTERUPDATE_FILES_BODY_DATA_STATUTE_OF_LIMITATIONS_STATUS_VALUES: set[
    MatterupdateFilesBodyDataStatuteOfLimitationsStatus
] = {
    "complete",
    "in_progress",
    "in_review",
    "pending",
}


def check_matterupdate_files_body_data_statute_of_limitations_status(
    value: str,
) -> MatterupdateFilesBodyDataStatuteOfLimitationsStatus:
    if value in MATTERUPDATE_FILES_BODY_DATA_STATUTE_OF_LIMITATIONS_STATUS_VALUES:
        return cast(MatterupdateFilesBodyDataStatuteOfLimitationsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MATTERUPDATE_FILES_BODY_DATA_STATUTE_OF_LIMITATIONS_STATUS_VALUES!r}"
    )
