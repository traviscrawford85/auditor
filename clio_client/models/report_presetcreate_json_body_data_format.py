from typing import Literal, cast

ReportPresetcreateJsonBodyDataFormat = Literal["csv", "html", "json", "pdf", "xlsx", "zip"]

REPORT_PRESETCREATE_JSON_BODY_DATA_FORMAT_VALUES: set[ReportPresetcreateJsonBodyDataFormat] = {
    "csv",
    "html",
    "json",
    "pdf",
    "xlsx",
    "zip",
}


def check_report_presetcreate_json_body_data_format(value: str) -> ReportPresetcreateJsonBodyDataFormat:
    if value in REPORT_PRESETCREATE_JSON_BODY_DATA_FORMAT_VALUES:
        return cast(ReportPresetcreateJsonBodyDataFormat, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_PRESETCREATE_JSON_BODY_DATA_FORMAT_VALUES!r}")
