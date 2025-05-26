from typing import Literal, cast

ReportSchedulecreateJsonBodyDataFrequency = Literal["daily", "monthly", "weekly"]

REPORT_SCHEDULECREATE_JSON_BODY_DATA_FREQUENCY_VALUES: set[ReportSchedulecreateJsonBodyDataFrequency] = {
    "daily",
    "monthly",
    "weekly",
}


def check_report_schedulecreate_json_body_data_frequency(value: str) -> ReportSchedulecreateJsonBodyDataFrequency:
    if value in REPORT_SCHEDULECREATE_JSON_BODY_DATA_FREQUENCY_VALUES:
        return cast(ReportSchedulecreateJsonBodyDataFrequency, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_SCHEDULECREATE_JSON_BODY_DATA_FREQUENCY_VALUES!r}"
    )
