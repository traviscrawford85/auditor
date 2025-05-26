from typing import Literal, cast

ReportScheduleBaseFrequency = Literal["daily", "monthly", "weekly"]

REPORT_SCHEDULE_BASE_FREQUENCY_VALUES: set[ReportScheduleBaseFrequency] = {
    "daily",
    "monthly",
    "weekly",
}


def check_report_schedule_base_frequency(value: str) -> ReportScheduleBaseFrequency:
    if value in REPORT_SCHEDULE_BASE_FREQUENCY_VALUES:
        return cast(ReportScheduleBaseFrequency, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_SCHEDULE_BASE_FREQUENCY_VALUES!r}")
