from typing import Literal, cast

ReportBaseState = Literal["completed", "empty", "failed", "in_progress", "not_started", "queued"]

REPORT_BASE_STATE_VALUES: set[ReportBaseState] = {
    "completed",
    "empty",
    "failed",
    "in_progress",
    "not_started",
    "queued",
}


def check_report_base_state(value: str) -> ReportBaseState:
    if value in REPORT_BASE_STATE_VALUES:
        return cast(ReportBaseState, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_BASE_STATE_VALUES!r}")
