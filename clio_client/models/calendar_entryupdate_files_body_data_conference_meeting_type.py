from typing import Literal, cast

CalendarEntryupdateFilesBodyDataConferenceMeetingType = Literal["zoom"]

CALENDAR_ENTRYUPDATE_FILES_BODY_DATA_CONFERENCE_MEETING_TYPE_VALUES: set[
    CalendarEntryupdateFilesBodyDataConferenceMeetingType
] = {
    "zoom",
}


def check_calendar_entryupdate_files_body_data_conference_meeting_type(
    value: str,
) -> CalendarEntryupdateFilesBodyDataConferenceMeetingType:
    if value in CALENDAR_ENTRYUPDATE_FILES_BODY_DATA_CONFERENCE_MEETING_TYPE_VALUES:
        return cast(CalendarEntryupdateFilesBodyDataConferenceMeetingType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALENDAR_ENTRYUPDATE_FILES_BODY_DATA_CONFERENCE_MEETING_TYPE_VALUES!r}"
    )
