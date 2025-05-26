from typing import Literal, cast

RemindercreateFilesBodyDataDurationUnit = Literal["days", "hours", "minutes", "weeks"]

REMINDERCREATE_FILES_BODY_DATA_DURATION_UNIT_VALUES: set[RemindercreateFilesBodyDataDurationUnit] = {
    "days",
    "hours",
    "minutes",
    "weeks",
}


def check_remindercreate_files_body_data_duration_unit(value: str) -> RemindercreateFilesBodyDataDurationUnit:
    if value in REMINDERCREATE_FILES_BODY_DATA_DURATION_UNIT_VALUES:
        return cast(RemindercreateFilesBodyDataDurationUnit, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMINDERCREATE_FILES_BODY_DATA_DURATION_UNIT_VALUES!r}"
    )
