from typing import Literal, cast

CalendarEntryupdateJsonBodyDataConferenceMeetingType = Literal["zoom"]

CALENDAR_ENTRYUPDATE_JSON_BODY_DATA_CONFERENCE_MEETING_TYPE_VALUES: set[
    CalendarEntryupdateJsonBodyDataConferenceMeetingType
] = {
    "zoom",
}


def check_calendar_entryupdate_json_body_data_conference_meeting_type(
    value: str,
) -> CalendarEntryupdateJsonBodyDataConferenceMeetingType:
    if value in CALENDAR_ENTRYUPDATE_JSON_BODY_DATA_CONFERENCE_MEETING_TYPE_VALUES:
        return cast(CalendarEntryupdateJsonBodyDataConferenceMeetingType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALENDAR_ENTRYUPDATE_JSON_BODY_DATA_CONFERENCE_MEETING_TYPE_VALUES!r}"
    )
