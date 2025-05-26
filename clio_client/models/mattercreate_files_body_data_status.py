from typing import Literal, cast

MattercreateFilesBodyDataStatus = Literal["closed", "open", "pending"]

MATTERCREATE_FILES_BODY_DATA_STATUS_VALUES: set[MattercreateFilesBodyDataStatus] = {
    "closed",
    "open",
    "pending",
}


def check_mattercreate_files_body_data_status(value: str) -> MattercreateFilesBodyDataStatus:
    if value in MATTERCREATE_FILES_BODY_DATA_STATUS_VALUES:
        return cast(MattercreateFilesBodyDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATTERCREATE_FILES_BODY_DATA_STATUS_VALUES!r}")
