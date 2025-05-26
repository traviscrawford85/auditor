from typing import Literal, cast

CalendarupdateDataBodyDataSource = Literal["mobile", "web"]

CALENDARUPDATE_DATA_BODY_DATA_SOURCE_VALUES: set[CalendarupdateDataBodyDataSource] = {
    "mobile",
    "web",
}


def check_calendarupdate_data_body_data_source(value: str) -> CalendarupdateDataBodyDataSource:
    if value in CALENDARUPDATE_DATA_BODY_DATA_SOURCE_VALUES:
        return cast(CalendarupdateDataBodyDataSource, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALENDARUPDATE_DATA_BODY_DATA_SOURCE_VALUES!r}")
