from typing import Literal, cast

CalendarEntrycreateFilesBodyDataDeleted = Literal["future", "single"]

CALENDAR_ENTRYCREATE_FILES_BODY_DATA_DELETED_VALUES: set[CalendarEntrycreateFilesBodyDataDeleted] = {
    "future",
    "single",
}


def check_calendar_entrycreate_files_body_data_deleted(value: str) -> CalendarEntrycreateFilesBodyDataDeleted:
    if value in CALENDAR_ENTRYCREATE_FILES_BODY_DATA_DELETED_VALUES:
        return cast(CalendarEntrycreateFilesBodyDataDeleted, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALENDAR_ENTRYCREATE_FILES_BODY_DATA_DELETED_VALUES!r}"
    )
