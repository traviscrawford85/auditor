from typing import Literal, cast

CalendarEntryupdateDataBodyDataConferenceMeetingType = Literal["zoom"]

CALENDAR_ENTRYUPDATE_DATA_BODY_DATA_CONFERENCE_MEETING_TYPE_VALUES: set[
    CalendarEntryupdateDataBodyDataConferenceMeetingType
] = {
    "zoom",
}


def check_calendar_entryupdate_data_body_data_conference_meeting_type(
    value: str,
) -> CalendarEntryupdateDataBodyDataConferenceMeetingType:
    if value in CALENDAR_ENTRYUPDATE_DATA_BODY_DATA_CONFERENCE_MEETING_TYPE_VALUES:
        return cast(CalendarEntryupdateDataBodyDataConferenceMeetingType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALENDAR_ENTRYUPDATE_DATA_BODY_DATA_CONFERENCE_MEETING_TYPE_VALUES!r}"
    )
