from typing import Literal, cast

ReportBaseFormat = Literal["csv", "html", "json", "pdf", "xlsx", "zip"]

REPORT_BASE_FORMAT_VALUES: set[ReportBaseFormat] = {
    "csv",
    "html",
    "json",
    "pdf",
    "xlsx",
    "zip",
}


def check_report_base_format(value: str) -> ReportBaseFormat:
    if value in REPORT_BASE_FORMAT_VALUES:
        return cast(ReportBaseFormat, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_BASE_FORMAT_VALUES!r}")
