from typing import Literal, cast

ReportPresetupdateDataBodyDataFormat = Literal["csv", "html", "json", "pdf", "xlsx", "zip"]

REPORT_PRESETUPDATE_DATA_BODY_DATA_FORMAT_VALUES: set[ReportPresetupdateDataBodyDataFormat] = {
    "csv",
    "html",
    "json",
    "pdf",
    "xlsx",
    "zip",
}


def check_report_presetupdate_data_body_data_format(value: str) -> ReportPresetupdateDataBodyDataFormat:
    if value in REPORT_PRESETUPDATE_DATA_BODY_DATA_FORMAT_VALUES:
        return cast(ReportPresetupdateDataBodyDataFormat, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_PRESETUPDATE_DATA_BODY_DATA_FORMAT_VALUES!r}")
