from typing import Literal, cast

ReportPresetindexScheduleFrequency = Literal["daily", "monthly", "weekly"]

REPORT_PRESETINDEX_SCHEDULE_FREQUENCY_VALUES: set[ReportPresetindexScheduleFrequency] = {
    "daily",
    "monthly",
    "weekly",
}


def check_report_presetindex_schedule_frequency(value: str) -> ReportPresetindexScheduleFrequency:
    if value in REPORT_PRESETINDEX_SCHEDULE_FREQUENCY_VALUES:
        return cast(ReportPresetindexScheduleFrequency, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_PRESETINDEX_SCHEDULE_FREQUENCY_VALUES!r}")
