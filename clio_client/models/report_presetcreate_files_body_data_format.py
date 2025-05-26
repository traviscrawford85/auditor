from typing import Literal, cast

ReportPresetcreateFilesBodyDataFormat = Literal["csv", "html", "json", "pdf", "xlsx", "zip"]

REPORT_PRESETCREATE_FILES_BODY_DATA_FORMAT_VALUES: set[ReportPresetcreateFilesBodyDataFormat] = {
    "csv",
    "html",
    "json",
    "pdf",
    "xlsx",
    "zip",
}


def check_report_presetcreate_files_body_data_format(value: str) -> ReportPresetcreateFilesBodyDataFormat:
    if value in REPORT_PRESETCREATE_FILES_BODY_DATA_FORMAT_VALUES:
        return cast(ReportPresetcreateFilesBodyDataFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPORT_PRESETCREATE_FILES_BODY_DATA_FORMAT_VALUES!r}"
    )
