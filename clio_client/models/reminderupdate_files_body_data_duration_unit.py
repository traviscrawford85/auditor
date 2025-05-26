from typing import Literal, cast

ReminderupdateFilesBodyDataDurationUnit = Literal["days", "hours", "minutes", "weeks"]

REMINDERUPDATE_FILES_BODY_DATA_DURATION_UNIT_VALUES: set[ReminderupdateFilesBodyDataDurationUnit] = {
    "days",
    "hours",
    "minutes",
    "weeks",
}


def check_reminderupdate_files_body_data_duration_unit(value: str) -> ReminderupdateFilesBodyDataDurationUnit:
    if value in REMINDERUPDATE_FILES_BODY_DATA_DURATION_UNIT_VALUES:
        return cast(ReminderupdateFilesBodyDataDurationUnit, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REMINDERUPDATE_FILES_BODY_DATA_DURATION_UNIT_VALUES!r}"
    )
