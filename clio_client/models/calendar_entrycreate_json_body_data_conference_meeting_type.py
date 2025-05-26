from typing import Literal, cast

CalendarEntrycreateJsonBodyDataConferenceMeetingType = Literal["zoom"]

CALENDAR_ENTRYCREATE_JSON_BODY_DATA_CONFERENCE_MEETING_TYPE_VALUES: set[
    CalendarEntrycreateJsonBodyDataConferenceMeetingType
] = {
    "zoom",
}


def check_calendar_entrycreate_json_body_data_conference_meeting_type(
    value: str,
) -> CalendarEntrycreateJsonBodyDataConferenceMeetingType:
    if value in CALENDAR_ENTRYCREATE_JSON_BODY_DATA_CONFERENCE_MEETING_TYPE_VALUES:
        return cast(CalendarEntrycreateJsonBodyDataConferenceMeetingType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALENDAR_ENTRYCREATE_JSON_BODY_DATA_CONFERENCE_MEETING_TYPE_VALUES!r}"
    )
