from typing import Literal, cast

ReportPresetBaseFormat = Literal["csv", "html", "json", "pdf", "xlsx", "zip"]

REPORT_PRESET_BASE_FORMAT_VALUES: set[ReportPresetBaseFormat] = {
    "csv",
    "html",
    "json",
    "pdf",
    "xlsx",
    "zip",
}


def check_report_preset_base_format(value: str) -> ReportPresetBaseFormat:
    if value in REPORT_PRESET_BASE_FORMAT_VALUES:
        return cast(ReportPresetBaseFormat, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_PRESET_BASE_FORMAT_VALUES!r}")
