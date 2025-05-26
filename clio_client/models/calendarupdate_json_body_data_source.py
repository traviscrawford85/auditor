from typing import Literal, cast

CalendarupdateJsonBodyDataSource = Literal["mobile", "web"]

CALENDARUPDATE_JSON_BODY_DATA_SOURCE_VALUES: set[CalendarupdateJsonBodyDataSource] = {
    "mobile",
    "web",
}


def check_calendarupdate_json_body_data_source(value: str) -> CalendarupdateJsonBodyDataSource:
    if value in CALENDARUPDATE_JSON_BODY_DATA_SOURCE_VALUES:
        return cast(CalendarupdateJsonBodyDataSource, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALENDARUPDATE_JSON_BODY_DATA_SOURCE_VALUES!r}")
