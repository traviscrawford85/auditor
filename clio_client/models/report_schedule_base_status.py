from typing import Literal, cast

ReportScheduleBaseStatus = Literal["completed", "failed", "initial", "processing", "queued"]

REPORT_SCHEDULE_BASE_STATUS_VALUES: set[ReportScheduleBaseStatus] = {
    "completed",
    "failed",
    "initial",
    "processing",
    "queued",
}


def check_report_schedule_base_status(value: str) -> ReportScheduleBaseStatus:
    if value in REPORT_SCHEDULE_BASE_STATUS_VALUES:
        return cast(ReportScheduleBaseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_SCHEDULE_BASE_STATUS_VALUES!r}")
