from typing import Literal, cast

CalendarEntrycreateFilesBodyDataConferenceMeetingType = Literal["zoom"]

CALENDAR_ENTRYCREATE_FILES_BODY_DATA_CONFERENCE_MEETING_TYPE_VALUES: set[
    CalendarEntrycreateFilesBodyDataConferenceMeetingType
] = {
    "zoom",
}


def check_calendar_entrycreate_files_body_data_conference_meeting_type(
    value: str,
) -> CalendarEntrycreateFilesBodyDataConferenceMeetingType:
    if value in CALENDAR_ENTRYCREATE_FILES_BODY_DATA_CONFERENCE_MEETING_TYPE_VALUES:
        return cast(CalendarEntrycreateFilesBodyDataConferenceMeetingType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALENDAR_ENTRYCREATE_FILES_BODY_DATA_CONFERENCE_MEETING_TYPE_VALUES!r}"
    )
