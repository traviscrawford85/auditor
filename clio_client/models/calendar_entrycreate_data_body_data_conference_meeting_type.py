from typing import Literal, cast

CalendarEntrycreateDataBodyDataConferenceMeetingType = Literal["zoom"]

CALENDAR_ENTRYCREATE_DATA_BODY_DATA_CONFERENCE_MEETING_TYPE_VALUES: set[
    CalendarEntrycreateDataBodyDataConferenceMeetingType
] = {
    "zoom",
}


def check_calendar_entrycreate_data_body_data_conference_meeting_type(
    value: str,
) -> CalendarEntrycreateDataBodyDataConferenceMeetingType:
    if value in CALENDAR_ENTRYCREATE_DATA_BODY_DATA_CONFERENCE_MEETING_TYPE_VALUES:
        return cast(CalendarEntrycreateDataBodyDataConferenceMeetingType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALENDAR_ENTRYCREATE_DATA_BODY_DATA_CONFERENCE_MEETING_TYPE_VALUES!r}"
    )
