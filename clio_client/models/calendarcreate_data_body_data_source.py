from typing import Literal, cast

CalendarcreateDataBodyDataSource = Literal["mobile", "web"]

CALENDARCREATE_DATA_BODY_DATA_SOURCE_VALUES: set[CalendarcreateDataBodyDataSource] = {
    "mobile",
    "web",
}


def check_calendarcreate_data_body_data_source(value: str) -> CalendarcreateDataBodyDataSource:
    if value in CALENDARCREATE_DATA_BODY_DATA_SOURCE_VALUES:
        return cast(CalendarcreateDataBodyDataSource, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CALENDARCREATE_DATA_BODY_DATA_SOURCE_VALUES!r}")
