from typing import Literal, cast

CalendarcreateJsonBodyDataSource = Literal["mobile", "web"]

CALENDARCREATE_JSON_BODY_DATA_SOURCE_VALUES: set[CalendarcreateJsonBodyDataSource] = {
    "mobile",
    "web",
}


def check_calendarcreate_json_body_data_source(value: str) -> CalendarcreateJsonBodyDataSource:
    if value in CALENDARCREATE_JSON_BODY_DATA_SOURCE_VALUES:
        return cast(CalendarcreateJsonBodyDataSource, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALENDARCREATE_JSON_BODY_DATA_SOURCE_VALUES!r}")
