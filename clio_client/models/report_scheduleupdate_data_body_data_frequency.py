from typing import Literal, cast

ReportScheduleupdateDataBodyDataFrequency = Literal["daily", "monthly", "weekly"]

REPORT_SCHEDULEUPDATE_DATA_BODY_DATA_FREQUENCY_VALUES: set[ReportScheduleupdateDataBodyDataFrequency] = {
    "daily",
    "monthly",
    "weekly",
}


def check_report_scheduleupdate_data_body_data_frequency(value: str) -> ReportScheduleupdateDataBodyDataFrequency:
    if value in REPORT_SCHEDULEUPDATE_DATA_BODY_DATA_FREQUENCY_VALUES:
        return cast(ReportScheduleupdateDataBodyDataFrequency, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_SCHEDULEUPDATE_DATA_BODY_DATA_FREQUENCY_VALUES!r}"
    )
