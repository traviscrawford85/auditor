from typing import Literal, cast

MatterupdateFilesBodyDataStatus = Literal["closed", "open", "pending"]

MATTERUPDATE_FILES_BODY_DATA_STATUS_VALUES: set[MatterupdateFilesBodyDataStatus] = {
    "closed",
    "open",
    "pending",
}


def check_matterupdate_files_body_data_status(value: str) -> MatterupdateFilesBodyDataStatus:
    if value in MATTERUPDATE_FILES_BODY_DATA_STATUS_VALUES:
        return cast(MatterupdateFilesBodyDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATTERUPDATE_FILES_BODY_DATA_STATUS_VALUES!r}")
