from typing import Literal, cast

CalendarEntryupdateFilesBodyDataDeleted = Literal["future", "single"]

CALENDAR_ENTRYUPDATE_FILES_BODY_DATA_DELETED_VALUES: set[CalendarEntryupdateFilesBodyDataDeleted] = {
    "future",
    "single",
}


def check_calendar_entryupdate_files_body_data_deleted(value: str) -> CalendarEntryupdateFilesBodyDataDeleted:
    if value in CALENDAR_ENTRYUPDATE_FILES_BODY_DATA_DELETED_VALUES:
        return cast(CalendarEntryupdateFilesBodyDataDeleted, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALENDAR_ENTRYUPDATE_FILES_BODY_DATA_DELETED_VALUES!r}"
    )
