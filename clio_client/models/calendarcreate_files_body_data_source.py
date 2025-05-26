from typing import Literal, cast

CalendarcreateFilesBodyDataSource = Literal["mobile", "web"]

CALENDARCREATE_FILES_BODY_DATA_SOURCE_VALUES: set[CalendarcreateFilesBodyDataSource] = {
    "mobile",
    "web",
}


def check_calendarcreate_files_body_data_source(value: str) -> CalendarcreateFilesBodyDataSource:
    if value in CALENDARCREATE_FILES_BODY_DATA_SOURCE_VALUES:
        return cast(CalendarcreateFilesBodyDataSource, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALENDARCREATE_FILES_BODY_DATA_SOURCE_VALUES!r}")
