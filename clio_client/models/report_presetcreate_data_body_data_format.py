from typing import Literal, cast

ReportPresetcreateDataBodyDataFormat = Literal["csv", "html", "json", "pdf", "xlsx", "zip"]

REPORT_PRESETCREATE_DATA_BODY_DATA_FORMAT_VALUES: set[ReportPresetcreateDataBodyDataFormat] = {
    "csv",
    "html",
    "json",
    "pdf",
    "xlsx",
    "zip",
}


def check_report_presetcreate_data_body_data_format(value: str) -> ReportPresetcreateDataBodyDataFormat:
    if value in REPORT_PRESETCREATE_DATA_BODY_DATA_FORMAT_VALUES:
        return cast(ReportPresetcreateDataBodyDataFormat, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REPORT_PRESETCREATE_DATA_BODY_DATA_FORMAT_VALUES!r}")
