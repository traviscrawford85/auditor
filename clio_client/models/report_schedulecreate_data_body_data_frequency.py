from typing import Literal, cast

ReportSchedulecreateDataBodyDataFrequency = Literal["daily", "monthly", "weekly"]

REPORT_SCHEDULECREATE_DATA_BODY_DATA_FREQUENCY_VALUES: set[ReportSchedulecreateDataBodyDataFrequency] = {
    "daily",
    "monthly",
    "weekly",
}


def check_report_schedulecreate_data_body_data_frequency(value: str) -> ReportSchedulecreateDataBodyDataFrequency:
    if value in REPORT_SCHEDULECREATE_DATA_BODY_DATA_FREQUENCY_VALUES:
        return cast(ReportSchedulecreateDataBodyDataFrequency, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_SCHEDULECREATE_DATA_BODY_DATA_FREQUENCY_VALUES!r}"
    )
