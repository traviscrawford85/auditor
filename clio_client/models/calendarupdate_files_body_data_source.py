from typing import Literal, cast

CalendarupdateFilesBodyDataSource = Literal["mobile", "web"]

CALENDARUPDATE_FILES_BODY_DATA_SOURCE_VALUES: set[CalendarupdateFilesBodyDataSource] = {
    "mobile",
    "web",
}


def check_calendarupdate_files_body_data_source(value: str) -> CalendarupdateFilesBodyDataSource:
    if value in CALENDARUPDATE_FILES_BODY_DATA_SOURCE_VALUES:
        return cast(CalendarupdateFilesBodyDataSource, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALENDARUPDATE_FILES_BODY_DATA_SOURCE_VALUES!r}")
