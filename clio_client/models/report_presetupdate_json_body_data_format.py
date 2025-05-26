from typing import Literal, cast

ReportPresetupdateJsonBodyDataFormat = Literal["csv", "html", "json", "pdf", "xlsx", "zip"]

REPORT_PRESETUPDATE_JSON_BODY_DATA_FORMAT_VALUES: set[ReportPresetupdateJsonBodyDataFormat] = {
    "csv",
    "html",
    "json",
    "pdf",
    "xlsx",
    "zip",
}


def check_report_presetupdate_json_body_data_format(value: str) -> ReportPresetupdateJsonBodyDataFormat:
    if value in REPORT_PRESETUPDATE_JSON_BODY_DATA_FORMAT_VALUES:
        return cast(ReportPresetupdateJsonBodyDataFormat, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_PRESETUPDATE_JSON_BODY_DATA_FORMAT_VALUES!r}")
