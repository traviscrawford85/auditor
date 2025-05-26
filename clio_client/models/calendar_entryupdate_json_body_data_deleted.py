from typing import Literal, cast

CalendarEntryupdateJsonBodyDataDeleted = Literal["future", "single"]

CALENDAR_ENTRYUPDATE_JSON_BODY_DATA_DELETED_VALUES: set[CalendarEntryupdateJsonBodyDataDeleted] = {
    "future",
    "single",
}


def check_calendar_entryupdate_json_body_data_deleted(value: str) -> CalendarEntryupdateJsonBodyDataDeleted:
    if value in CALENDAR_ENTRYUPDATE_JSON_BODY_DATA_DELETED_VALUES:
        return cast(CalendarEntryupdateJsonBodyDataDeleted, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALENDAR_ENTRYUPDATE_JSON_BODY_DATA_DELETED_VALUES!r}"
    )
