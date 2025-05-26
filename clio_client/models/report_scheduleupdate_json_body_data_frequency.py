from typing import Literal, cast

ReportScheduleupdateJsonBodyDataFrequency = Literal["daily", "monthly", "weekly"]

REPORT_SCHEDULEUPDATE_JSON_BODY_DATA_FREQUENCY_VALUES: set[ReportScheduleupdateJsonBodyDataFrequency] = {
    "daily",
    "monthly",
    "weekly",
}


def check_report_scheduleupdate_json_body_data_frequency(value: str) -> ReportScheduleupdateJsonBodyDataFrequency:
    if value in REPORT_SCHEDULEUPDATE_JSON_BODY_DATA_FREQUENCY_VALUES:
        return cast(ReportScheduleupdateJsonBodyDataFrequency, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_SCHEDULEUPDATE_JSON_BODY_DATA_FREQUENCY_VALUES!r}"
    )
