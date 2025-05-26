from typing import Literal, cast

CalendarEntryupdateDataBodyDataDeleted = Literal["future", "single"]

CALENDAR_ENTRYUPDATE_DATA_BODY_DATA_DELETED_VALUES: set[CalendarEntryupdateDataBodyDataDeleted] = {
    "future",
    "single",
}


def check_calendar_entryupdate_data_body_data_deleted(value: str) -> CalendarEntryupdateDataBodyDataDeleted:
    if value in CALENDAR_ENTRYUPDATE_DATA_BODY_DATA_DELETED_VALUES:
        return cast(CalendarEntryupdateDataBodyDataDeleted, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALENDAR_ENTRYUPDATE_DATA_BODY_DATA_DELETED_VALUES!r}"
    )
