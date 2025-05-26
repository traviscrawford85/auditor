from typing import Literal, cast

ReportBaseSource = Literal["presets", "reports", "scheduled"]

REPORT_BASE_SOURCE_VALUES: set[ReportBaseSource] = {
    "presets",
    "reports",
    "scheduled",
}


def check_report_base_source(value: str) -> ReportBaseSource:
    if value in REPORT_BASE_SOURCE_VALUES:
        return cast(ReportBaseSource, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_BASE_SOURCE_VALUES!r}")
